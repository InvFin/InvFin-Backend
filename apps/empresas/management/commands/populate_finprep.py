from django.core.management import BaseCommand

from apps.general.constants import PERIOD_FOR_YEAR
from apps.general.models import Period
from apps.empresas.models import (
    Company,
    BalanceSheetFinprep,
    IncomeStatementFinprep,
    CashflowStatementFinprep
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for company in Company.objects.clean_companies():
            for company_data in company.inc_statements.all().values():
                date = company_data["date"]
                period, created = Period.objects.get_or_create(year=date, period=PERIOD_FOR_YEAR)
                company_data.pop("id")
                company_data["period_id"] = period.id
                IncomeStatementFinprep.objects.create(
                    cost_and_expenses=company_data.pop("cost_and_expenses"),
                    cost_of_revenue=company_data.pop("cost_of_revenue"),
                    depreciation_and_amortization=company_data.pop("depreciation_amortization"),
                    ebitda=company_data.pop("ebitda"),
                    general_and_administrative_expenses=company_data.pop("general_administrative_expenses"),
                    gross_profit=company_data.pop("gross_profit"),
                    income_before_tax=company_data.pop("income_before_tax"),
                    income_tax_expense=company_data.pop("income_tax_expenses"),
                    interest_expense=company_data.pop("interest_expense"),
                    net_income=company_data.pop("net_income"),
                    operating_expenses=company_data.pop("operating_expenses"),
                    operating_income=company_data.pop("operating_income"),
                    other_expenses=company_data.pop("other_expenses"),
                    research_and_development_expenses=company_data.pop("rd_expenses"),
                    revenue=company_data.pop("revenue"),
                    selling_and_marketing_expenses=company_data.pop("selling_marketing_expenses"),
                    selling_general_and_administrative_expenses=company_data.pop("sga_expenses"),
                    total_other_income_expenses_net=company_data.pop("net_total_other_income_expenses"),
                    weighted_average_shs_out=company_data.pop("weighted_average_shares_outstanding"),
                    weighted_average_shs_out_dil=company_data.pop("weighted_average_diluated_shares_outstanding"),
                    **company_data
                )
            for company_data in company.balance_sheets.all().values():
                date = company_data["date"]
                period, created = Period.objects.get_or_create(year=date, period=PERIOD_FOR_YEAR)
                company_data.pop("id")
                company_data["period_id"] = period.id
                BalanceSheetFinprep.objects.create(
                    property_plant_equipment_net=company_data.pop("property_plant_equipment"),
                    common_stock=company_data.pop("common_stocks"),
                    **company_data
                )
            for company_data in company.cf_statements.all().values():
                date = company_data["date"]
                period, created = Period.objects.get_or_create(year=date, period=PERIOD_FOR_YEAR)
                company_data.pop("id")
                company_data["period_id"] = period.id
                CashflowStatementFinprep.objects.create(
                    depreciation_and_amortization=company_data.pop("depreciation_amortization"),
                    stock_based_compensation=company_data.pop("stock_based_compesation"),
                    accounts_payables=company_data.pop("accounts_payable"),
                    operating_cash_flow=company_data.pop("operating_cf"),
                    free_cash_flow=company_data.pop("fcf"),
                    capital_expenditure=company_data.pop("capex"),
                    net_cash_provided_by_operating_activities=company_data.pop("operating_activities_cf"),
                    net_cash_used_for_investing_activites=company_data.pop("investing_activities_cf"),
                    net_cash_used_provided_by_financing_activities=company_data.pop("financing_activities_cf"),
                    investments_in_property_plant_and_equipment=company_data.pop("investments_property_plant_equipment"),
                    purchases_of_investments=company_data.pop("purchases_investments"),
                    sales_maturities_of_investments=company_data.pop("sales_maturities_investments"),
                    effect_of_forex_changes_on_cash=company_data.pop("effect_forex_exchange"),
                    other_financing_activites=company_data.pop("other_financing_activities"),
                    net_change_in_cash=company_data.pop("net_change_cash"),
                    cash_at_end_of_period=company_data.pop("cash_end_period"),
                    cash_at_beginning_of_period=company_data.pop("cash_beginning_period"),
                    **company_data
                )
