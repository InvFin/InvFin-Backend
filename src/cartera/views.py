from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from src.seo.views import SEOTemplateView

from .models import Patrimonio

User = get_user_model()


class DefaultCateraView(LoginRequiredMixin, SEOTemplateView):
    no_index = True
    no_follow = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        patrimoine = Patrimonio.objects.get_or_create(user=user)[0]
        context["patrimonio"] = patrimoine
        context["meta_title"] = self.meta_title
        return context


class InicioCarteraView(DefaultCateraView):
    template_name = "private/cartera_inicio.html"
    meta_title = "Tu gestor patrimonial"


class InicioPortfolioView(DefaultCateraView):
    template_name = "private/cartera.html"
    meta_title = "Tu cartera"


class InicioCashflowView(DefaultCateraView):
    template_name = "private/financials.html"
    meta_title = "Tus finanzas"


def return_balance_table(request):
    user = request.user
    overall_portfolio_information = user.user_patrimoine.overall_portfolio_information
    return render(request, "tables/balance.html", {"overall_portfolio_information": overall_portfolio_information})
