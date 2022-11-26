from typing import Dict
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView

from apps.empresas.outils.update import UpdateCompany
from apps.empresas.models import Company, ExchangeOrganisation
from apps.empresas.utils import company_searched, FinprepRequestCheck
from apps.etfs.models import Etf
from apps.seo.views import SEODetailView, SEOListView
from apps.users import constants as users_constants
from apps.users.models import CreditUsageHistorial

from apps.screener.models import CompanyInformationBought, YahooScreener


class CompanyLookUpView(RedirectView):
    def get(self, request, *args, **kwargs):
        company = self.request.GET["stock"]
        path = company_searched(company, self.request)
        return HttpResponseRedirect(path)


class ScreenerInicioView(SEOListView):
    model = ExchangeOrganisation
    context_object_name = "organisations"
    template_name = "screener_inicio.html"
    meta_description = (
        "Estudia todos loas activos que quieras para ser el mejor inversor. Ten acceso a más de 30000 empresas y 30"
        " años de información."
    )
    meta_tags = "empresas, inversiones, analisis de empresas, invertir"
    meta_title = "Más de 30 años de información financiera de cualquier activo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["screeners"] = YahooScreener.objects.all()
        return context


class CompanyScreenerInicioView(SEOListView):
    model = Company
    template_name = "empresas/company_inicio.html"
    context_object_name = "empresas"
    paginate_by = 50
    slug_url_kwarg = "slug"
    meta_description = (
        "Estudia todas las empresas que quieras para ser el mejor inversor. Ten acceso a más de 30000 empresas y 30"
        " años de información."
    )
    meta_tags = "empresas, inversiones, analisis de empresas, invertir"
    # meta_title =

    def get_queryset(self, **kwargs):
        return Company.objects.clean_companies_by_main_exchange(self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.kwargs["slug"]
        context["meta_title"] = f"Más de 30 años de información financiera de cualquier empresa de {name}"
        context["meta_url"] = f"/empresas-de/{name}/"
        return context


class AllYahooScreenersView(SEOListView):
    model = YahooScreener
    template_name = "yahoo-screeners/all-screeners.html"
    context_object_name = "screeners"
    meta_title = "Los mejores screeners"


class YahooScreenerView(SEODetailView):
    model = YahooScreener
    template_name = "yahoo-screeners/screener.html"
    context_object_name = "screener"
    slug_url_kwarg = "slug"
    slug_field = "slug"
    meta_tags = "empresas, inversiones, analisis de empresas, invertir"


class EtfScreenerInicioView(ListView):
    model = Etf
    template_name = "etfs/inicio.html"
    context_object_name = "etfs"


class CompanyDetailsView(SEODetailView):
    model = Company
    template_name = "empresas/company_detail.html"
    context_object_name = "the_company"
    slug_field = "ticker"

    def get_object(self):
        ticker = self.kwargs.get("ticker")
        try:
            response = Company.objects.prefetch_yearly_historical_data(ticker=ticker)
            self.object = response
            return response
        except Company.DoesNotExist:
            response, created = Company.objects.get_or_create(name="Need-parsing", ticker=ticker)
            return None
        except Exception:
            """
            TODO
            Use logger to know the problem
            """
            return None

    def save_company_in_session(self, empresa):
        if "companies_visited" not in self.request.session:
            companies_visited = self.request.session["companies_visited"] = []
        else:
            companies_visited = self.request.session["companies_visited"]
        tickers = [ticker["ticker"] for ticker in companies_visited]
        if empresa.ticker not in tickers:
            companies_visited.append(
                {
                    "ticker": empresa.ticker,
                    "img": empresa.image,
                    "sector_id": empresa.sector.id,
                    "industry_id": empresa.industry.id,
                    "country_id": empresa.country.id,
                    "exchange_id": empresa.exchange.id,
                }
            )
        if len(companies_visited) > 10:
            companies_visited.pop(0)
        self.request.session.modified = True

    def check_company_for_updates(self, empresa) -> None:
        if FinprepRequestCheck().manage_track_requests(3):
            if not empresa.has_checking("fixed_last_finprep"):
                UpdateCompany(empresa).create_financials_finprep()

    def get_meta_description(self, empresa) -> str:
        return (
            f"Estudia a fondo la empresa {empresa.name}. Más de 30 años de información, noticias, análisis FODA y"
            " mucho más"
        )

    def get_meta_tags(self) -> str:
        return f"finanzas, blog financiero, blog el financiera, invertir, {self.object.name}, {self.object.ticker}"

    def get_meta_title(self, empresa) -> str:
        return f"Análisis completo de {empresa.name}"

    def check_user_company_relation(self, object: Company, context: Dict) -> Dict:
        company_is_fav = False
        limit_years = 5
        has_bought = False
        user = self.request.user
        if user.is_authenticated:
            if object.ticker in user.fav_stocks.only("ticker"):
                company_is_fav = True
            if CompanyInformationBought.objects.filter(user=user, company=object).exists():
                limit_years = 0
                has_bought = True

        context["has_bought"] = has_bought
        context["company_is_fav"] = company_is_fav
        context["complete_info"] = object.complete_info(limit_years)
        return context

    def get_context_data(self, object, **kwargs):
        context = super().get_context_data(**kwargs)
        self.check_company_for_updates(object)
        self.save_company_in_session(object)
        self.get_meta_description(object)
        self.get_meta_tags()
        self.get_meta_title(object)
        context = self.check_user_company_relation(object, context)
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object:
            messages.error(
                self.request,
                "Lo sentimos, esta empresa todavía no tiene información ahora mismo vamos a recabar información y"
                " estará lista en poco tiempo",
            )
            return redirect(reverse("screener:screener_inicio"))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BuyCompanyInfo(RedirectView):
    def get(self, request, *args, **kwargs):
        company = Company.objects.get(id=self.request.GET["company_id"])
        user = request.user
        CreditUsageHistorial.objects.update_credits(
            user, 10, users_constants.BOUGHT_COMPANY_INFO, users_constants.REDUCE, company
        )
        CompanyInformationBought.objects.create(user=user, company=company)
        messages.success(
            request,
            f"Ahora que conoces toda la historia financiera de {company.name}, no olvides hacer un análisis FODA",
        )
        return redirect(reverse("screener:company", kwargs={"ticker": company.ticker}))


class EtfDetailsView(DetailView):
    model = Etf
    template_name = "etfs/details.html"
    context_object_name = "etf"
    slug_field = "ticker"

    def get_object(self):
        ticker = self.kwargs.get("ticker")
        return get_object_or_404(Etf, ticker=ticker)
