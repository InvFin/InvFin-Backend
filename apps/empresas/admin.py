from django.contrib import admin

from .models import (
    CashflowStatement,
    IncomeStatement,
    BalanceSheet,
    Company,
    CompanyGrowth,
    EficiencyRatio,
    EnterpriseValueRatio,
    Exchange,
    ExchangeOrganisation,
    RentabilityRatio,
    MarginRatio,
    PriceToRatio,
    LiquidityRatio,
    OperationRiskRatio,
    FreeCashFlowRatio,
    PerShareValue,
    CompanyStockPrice,
    NonGaap
)

from .utils import UpdateCompany

@admin.register(CashflowStatement)
class CashflowStatementAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(IncomeStatement)
class IncomeStatementAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(BalanceSheet)
class BalanceSheetAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.action(description='Put logos')
def find_logos(modeladmin, request, queryset):
    for query in queryset:
        UpdateCompany(query).add_logo()


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    actions = [find_logos]

    list_display = [
        'id',
        'name',
        'no_incs',
        'no_bs',
        'no_cfs',
        'description_translated',
        'has_logo',
    ]
    list_filter = [
        'no_incs',
        'no_bs',
        'no_cfs',
        'description_translated',
        'has_logo',
        'exchange__main_org',
    ]
    list_editable = [
        'no_incs',
        'no_bs',
        'no_cfs',
        'description_translated',
        'has_logo',
    ]
    search_fields = ['name', 'ticker']


@admin.register(CompanyGrowth)
class CompanyGrowthAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(EficiencyRatio)
class EficiencyRatioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(EnterpriseValueRatio)
class EnterpriseValueRatioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'exchange_ticker',
        'exchange',
        'country',
        'main_org'
    ]
    search_fields = ['main_org_name']


@admin.register(ExchangeOrganisation)
class ExchangeOrganisationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'image',
        'sub_exchange1',
        'sub_exchange2',
        'order',
    ]
    list_editable = ['order']
    search_fields = ['name']


@admin.register(RentabilityRatio)
class RentabilityRatioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(MarginRatio)
class MarginRatioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(PriceToRatio)
class PriceToRatioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(LiquidityRatio)
class LiquidityRatioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(OperationRiskRatio)
class OperationRiskRatioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(FreeCashFlowRatio)
class FreeCashFlowRatioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(PerShareValue)
class PerShareValueAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']


@admin.register(CompanyStockPrice)
class CompanyStockPriceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company_related',
        'date'
    ]
    search_fields = ['company_related_name']


@admin.register(NonGaap)
class NonGaapAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'date'
    ]
    search_fields = ['company_name']

