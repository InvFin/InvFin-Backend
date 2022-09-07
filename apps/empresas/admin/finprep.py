from django.contrib import admin

from apps.empresas.admin.base import BaseCompanyAdmin, BaseJSONWidgetInline
from apps.empresas.admin.filters.base import HasQuarterFilter

from apps.empresas.models import (
    BalanceSheetFinprep,
    CashflowStatementFinprep,
    IncomeStatementFinprep,
    CompanyFinprepProxy
)


class HasFinprepQuarterFilter(HasQuarterFilter):
    statements = [
        IncomeStatementFinprep,
        BalanceSheetFinprep,
        CashflowStatementFinprep,
    ]


class IncomeStatementFinprepInline(BaseJSONWidgetInline):
    model = IncomeStatementFinprep
    jazzmin_tab_id = "income-statement"


class BalanceSheetFinprepInline(BaseJSONWidgetInline):
    model = BalanceSheetFinprep
    jazzmin_tab_id = "balance-sheet"


class CashflowStatementFinprepInline(BaseJSONWidgetInline):
    model = CashflowStatementFinprep
    jazzmin_tab_id = "cashflow-statement"


@admin.register(CompanyFinprepProxy)
class CompanyFinprepProxyAdmin(BaseCompanyAdmin):
    inlines = [
        IncomeStatementFinprepInline,
        BalanceSheetFinprepInline,
        CashflowStatementFinprepInline
    ]

    list_filter = BaseCompanyAdmin.list_filter + [
        HasFinprepQuarterFilter
    ]