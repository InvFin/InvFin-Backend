from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from apps.general import constants as general_constants
from apps.general.forms import DefaultNewsletterForm
from apps.notifications.tasks import prepare_notification_task
from apps.public_blog.forms import PublicBlogForm
from apps.public_blog.models import NewsletterFollowers, PublicBlog, PublicBlogAsNewsletter, WritterProfile
from apps.seo.views import SEODetailView, SEOListView

User = get_user_model()


def following_management_view(request):
    redirect_to = reverse("users:user_inicio")
    if request.POST:
        writter = request.POST["writter"]
        action = request.POST["what"]
        writter = User.objects.get(id=writter)
        follower = User.objects.get_or_create_quick_user(request, just_newsletter=True)
        update_follower = writter.update_followers(follower, action)
        redirect_to = request.META.get("HTTP_REFERER")
        if update_follower == "already follower":
            messages.success(request, f"Ya estás siguiendo a {writter.full_name}")
            return redirect(redirect_to)

        prepare_notification_task.delay(writter.dict_for_task, general_constants.NEW_FOLLOWER)
        messages.success(request, f"A partir de ahora recibirás las newsletters de {writter.full_name}")
    return redirect(redirect_to)


@login_required
def user_become_writter_view(request):
    if request.method == "POST":
        domain = request.POST["domain"].lower()
        WritterProfile.objects.create(user=request.user, host_name=domain)
        request.user.is_writter = True
        request.user.save(update_fields=["is_writter"])
        NewsletterFollowers.objects.create(user=request.user)
        messages.success(
            request,
            "Pon al día tu perfil, añade tus redes sociales, una buena descripción y tu nombre para que la gente"
            " pueda conocerte.",
        )
        return redirect("users:update")


class PublicBlogsListView(SEOListView):
    model = PublicBlog
    template_name = "blog_inicio.html"
    ordering = ["-published_at"]
    context_object_name = "blogs"
    meta_description = "El blog donde tu también puedes escribir de forma libre"
    meta_tags = "finanzas, blog financiero, blog el financiera, invertir"
    meta_title = "Convíertete en escritor"

    def get_queryset(self):
        return PublicBlog.objects.filter(status=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["escritores"] = WritterProfile.objects.all()
        return context


class PublicBlogDetailsView(SEODetailView):
    model = PublicBlog
    template_name = "blog_details.html"
    context_object_name = "object"
    slug_field = "slug"
    is_article = True
    open_graph_type = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.update_views(self.get_object())
        return context


class WritterOnlyMixin(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin):
    def test_func(self):
        return self.request.user.is_writter

    def handle_no_permission(self):
        return redirect("public_blog:blog_list")


class WritterOwnBlogsListView(WritterOnlyMixin, SEODetailView):
    model = User
    template_name = "profile/manage_blogs.html"
    ordering = ["-published_at"]
    slug_field = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        writter = self.get_object()
        context["blogs"] = PublicBlog.objects.filter(author=writter).order_by("-created_at")
        context["meta_desc"] = "El blog donde tu también puedes escribir de forma libre"
        context["meta_tags"] = "finanzas, blog financiero, blog el financiera, invertir"
        context["meta_title"] = "Dashboard"
        context["meta_url"] = f"management/escritos/{writter.username}/"
        return context


class CreatePublicBlogPostView(WritterOnlyMixin, CreateView):
    model = PublicBlog
    form_class = PublicBlogForm
    success_message = "Escrito creado"
    template_name = "forms/manage_escrito.html"

    def get_context_data(self, **kwargs):
        context = super(CreatePublicBlogPostView, self).get_context_data(**kwargs)
        context["meta_title"] = "Dashboard"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        tags = self.request.POST["tags"].split(",")
        modelo = form.save()
        modelo.add_tags(tags)
        modelo.save_secondary_info("blog")
        if modelo.send_as_newsletter == True:
            # Prepare email and send it
            return redirect("public_blog:create_newsletter_blog", kwargs={"slug": modelo.slug})
        if modelo.status == general_constants.BASE_ESCRITO_PUBLISHED:
            prepare_notification_task.delay(modelo.dict_for_task, general_constants.NEW_BLOG_POST)
        return super(CreatePublicBlogPostView, self).form_valid(form)


class UpdatePublicBlogPostView(WritterOnlyMixin, UpdateView):
    model = PublicBlog
    form_class = PublicBlogForm
    success_message = "Escrito actualizado"
    template_name = "forms/manage_escrito.html"

    def get_success_url(self) -> str:
        return redirect("public_blog:manage_blogs", kwargs={"slug": self.request.user.username})

    def get_context_data(self, **kwargs):
        context = super(UpdatePublicBlogPostView, self).get_context_data(**kwargs)
        context["tags"] = self.get_object().tags.all()
        context["meta_title"] = "Dashboard"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        tags = self.request.POST["tags"].split(",")
        modelo = form.save()
        modelo.add_tags(tags)
        if modelo.send_as_newsletter:
            return redirect("public_blog:create_newsletter_blog", kwargs={"slug": modelo.slug})
        if modelo.status == general_constants.BASE_ESCRITO_PUBLISHED:
            prepare_notification_task.delay(modelo.dict_for_task, general_constants.NEW_BLOG_POST)
        return super(UpdatePublicBlogPostView, self).form_valid(form)

    def test_func(self):
        return self.get_object().author == self.request.user


@login_required
def create_newsletter_for_blog(request, slug):
    user = request.user
    blog = PublicBlog.objects.get(slug=slug)
    initial_form_values = {
        "title": blog.title,
        "content": blog.content,
    }
    newsletter_form = DefaultNewsletterForm(initial=initial_form_values)
    context = {"blog": blog, "newsletter_form": newsletter_form, "meta_title": "Dashboard"}
    if blog.author == user:
        if request.POST:
            newsletter_form = DefaultNewsletterForm(request.POST)
            messages.success(request, "Newsletter creada")
            return redirect("public_blog:manage_blogs", kwargs={"slug": user.username})
        return render(request, "forms/create_newsletter.html", context)
    else:
        return redirect("public_blog:blog_details", kwargs={"slug": blog.slug})


class UpdateBlogNewsletterView(WritterOnlyMixin, UpdateView):
    model = PublicBlogAsNewsletter
    context_object_name = "newsletter_form"
    success_message = "Escrito actualizado"
    template_name = "forms/update_newsletter.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["update"] = True
        context["tags"] = self.get_object().blog_related.tags.all()
        context["meta_title"] = "Dashboard"
        return

    def test_func(self):
        return self.get_object().blog_related.author == self.request.user
