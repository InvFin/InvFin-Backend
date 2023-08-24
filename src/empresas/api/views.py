from src.api.pagination import StandardResultPagination
from src.api.views import BaseAPIView, BasePublicAPIView
from src.empresas.api.serializers import (
    BalanceSheetSerializer,
    BasicCompanySerializer,
    CashflowStatementSerializer,
    CompanySerializer,
    ExchangeSerializer,
    IncomeStatementSerializer,
)
from src.empresas.models import (
    BalanceSheet,
    CashflowStatement,
    Company,
    Exchange,
    IncomeStatement,
)


class PublicCompanyAPIView(BasePublicAPIView):
    many_serializer_class = BasicCompanySerializer
    single_serializer_class = CompanySerializer
    many_queryset = Company.objects.select_related_information().all()
    single_queryset = Company.objects.api_query().all()
    lookup_field = "ticker"


class AllExchangesAPIView(BaseAPIView):
    serializer_class = ExchangeSerializer
    queryset = (Exchange.objects.all, True)
    pagination_class = StandardResultPagination
    model_to_track = "ignore"


class BasicCompanyAPIView(BaseAPIView):
    serializer_class = BasicCompanySerializer
    url_parameters = ["ticker"]
    model_to_track = Company


class CompleteCompanyAPIView(BaseAPIView):
    serializer_class = CompanySerializer
    queryset = (Company.objects.fast_full, False)
    url_parameters = ["ticker"]
    model_to_track = Company


class CompanyIncomeStatementAPIView(BaseAPIView):
    serializer_class = IncomeStatementSerializer
    limited = True
    url_parameters = ["ticker"]
    queryset = (IncomeStatement.objects.yearly_exclude_ttm, True)
    fk_lookup_model = "company__ticker"
    model_to_track = Company


class CompanyBalanceSheetAPIView(BaseAPIView):
    serializer_class = BalanceSheetSerializer
    limited = True
    queryset = (BalanceSheet.objects.yearly_exclude_ttm, True)
    url_parameters = ["ticker"]
    fk_lookup_model = "company__ticker"
    model_to_track = Company


class CompanyCashflowStatementAPIView(BaseAPIView):
    serializer_class = CashflowStatementSerializer
    limited = True
    queryset = (CashflowStatement.objects.yearly_exclude_ttm, True)
    url_parameters = ["ticker"]
    fk_lookup_model = "company__ticker"
    model_to_track = Company
