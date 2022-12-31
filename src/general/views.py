import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, RedirectView, TemplateView

from src.empresas.models import Company
from src.escritos.models import FavoritesTermsHistorial, FavoritesTermsList, Term
from src.notifications.models import Notification
from src.screener.models import FavoritesStocksHistorial
from src.super_investors.models import FavoritesSuperinvestorsHistorial, FavoritesSuperinvestorsList, Superinvestor


class MessagesTemplateview(TemplateView):
    template_name = "complements/messages.html"


def handler403(request, exception):
    return render(request, "errors/403.html")


def handler500(request):
    return render(request, "errors/500.html")


class Handler404(TemplateView):
    template_name = "errors/404.html"

    def handle_wrong_urls(self):
        if settings.FULL_DOMAIN in self.request.get_full_path_info():
            full_path = self.request.build_absolute_uri()
            full_path = full_path.replace(f"{settings.FULL_DOMAIN}/{settings.FULL_DOMAIN}", settings.FULL_DOMAIN)
            return full_path
        return None

    def get(self, request, *args, **kwargs):
        corrected_url = self.handle_wrong_urls()
        if corrected_url:
            return HttpResponseRedirect(corrected_url)
        return super().get(request, *args, **kwargs)


def suggest_list_search(request):
    if request.is_ajax():
        query = request.GET.get("term", "")
        companies_availables = Company.objects.filter(
            Q(name__icontains=query) | Q(ticker__icontains=query),
            no_incs=False,
            no_bs=False,
            no_cfs=False,
        )[:4]

        # terms_availables = Term.objects.filter(Q(title__icontains=query), status = 1)[:3]
        terms_availables = Term.objects.filter(Q(title__icontains=query))[:4]

        results = []
        for company in companies_availables:
            result = f"Empresa: {company.name} [{company.ticker}]"
            results.append(result)

        for term in terms_availables:
            result = f"Término: {term.title}"
            results.append(result)

        data = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data, mimetype)


def search_results(request):
    redirect_to = request.META.get("HTTP_REFERER")
    if request.POST:
        term = request.POST["term"]
        query = term[:7]
        if query == "Empresa":
            empresa_ticker = term.split(" [")[1]
            ticker = empresa_ticker[:-1]
            empresa_busqueda = Company.objects.get(ticker=ticker)
            redirect_to = empresa_busqueda.get_absolute_url()

        elif query == "Término":
            title = term.split(":")[1]
            title = title[1:]
            try:
                term_busqueda = Term.objects.get(title=title)
            except Term.MultipleObjectsReturned:
                term_busqueda = Term.objects.filter(title=title).first()
            redirect_to = term_busqueda.get_absolute_url()

        else:
            if term.isupper():
                empresa_busqueda = Company.objects.filter(ticker=term)
                if empresa_busqueda.exists():
                    redirect_to = empresa_busqueda[0].get_absolute_url()
            elif term.isupper() is False:
                empresa_busqueda = Company.objects.filter(name__icontains=term)
                if empresa_busqueda.exists():
                    redirect_to = empresa_busqueda[0].get_absolute_url()
            else:
                messages.warning(request, "No hemos entendido tu búsqueda")
    return redirect(redirect_to)


@login_required
def update_favorites(request):
    user = request.user

    if request.method == "POST":
        data = json.load(request)

        if "ticker" in data.keys():
            ticker = data.get("ticker")
            current_stock = Company.objects.get(ticker=ticker)

            if current_stock in user.fav_stocks:
                user.favorites_companies.stock.remove(current_stock)
                FavoritesStocksHistorial.objects.create(user=user, asset=current_stock, removed=True)
                is_favorite = False
            else:
                FavoritesStocksHistorial.objects.create(user=user, asset=current_stock, added=True)
                user.favorites_companies.stock.add(current_stock)
                is_favorite = True

        elif "term" in data.keys():
            term_id = data.get("term")
            current_term = Term.objects.get(id=term_id)
            try:
                user.favorites_terms
            except Exception:
                FavoritesTermsList.objects.create(user=user)
            if current_term in user.fav_terms:
                user.favorites_terms.term.remove(current_term)
                FavoritesTermsHistorial.objects.create(user=user, term=current_term, removed=True)
                is_favorite = False
            else:
                FavoritesTermsHistorial.objects.create(user=user, term=current_term, added=True)
                user.favorites_terms.term.add(current_term)
                is_favorite = True

        elif "investor" in data.keys():
            superinvestor = data.get("investor")
            current_superinvestor = Superinvestor.objects.get(slug=superinvestor)
            try:
                user.favorites_superinvestors
            except Exception:
                FavoritesSuperinvestorsList.objects.create(user=user)
            if current_superinvestor in user.fav_superinvestors:
                user.favorites_superinvestors.superinvestor.remove(current_superinvestor)
                FavoritesSuperinvestorsHistorial.objects.create(
                    user=user, superinvestor=current_superinvestor, removed=True
                )
                is_favorite = False
            else:
                FavoritesSuperinvestorsHistorial.objects.create(
                    user=user, superinvestor=current_superinvestor, added=True
                )
                user.favorites_superinvestors.superinvestor.add(current_superinvestor)
                is_favorite = True

        return JsonResponse({"is_favorite": is_favorite})


class ComingSoonview(TemplateView):
    template_name = "complements/coming_soon.html"


class NotificationsListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = "notifications/notifications_page.html"

    def get_queryset(self):
        notifications = Notification.objects.filter(user=self.request.user)
        notifications.update(is_seen=True)
        return notifications


class NotificationRedirectView(RedirectView):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@login_required(login_url="login")
def delete_notification(request, notif_id):
    user = request.user
    Notification.objects.get(id=notif_id, user=user).delete()
    return redirect("general:notifications_list")
