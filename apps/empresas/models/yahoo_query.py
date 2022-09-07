from django.db.models import (
    FloatField,
    DateTimeField,
    CharField,
    JSONField,
    DateTimeField
)

from apps.empresas.models import BaseStatement
from apps.empresas.extensions.yahoo_query import (
    IncomeStatementYahooQueryExtended,
    BalanceSheetYahooQueryExtended,
    CashflowStatementYahooQueryExtended
)


class BaseUnknownField(BaseStatement):
    financials = JSONField(default=dict)

    class Meta:
        abstract = True


class IncomeStatementYahooQuery(BaseUnknownField, IncomeStatementYahooQueryExtended):
    as_of_date = DateTimeField(blank=True, null=True)
    period_type = CharField(max_length=10, blank=True, null=True)
    currency_code = CharField(max_length=10, blank=True, null=True)
    basic_average_shares = FloatField(default=0, blank=True, null=True)
    basic_eps = FloatField(default=0, blank=True, null=True)
    cost_of_revenue = FloatField(default=0, blank=True, null=True)
    diluted_average_shares = FloatField(default=0, blank=True, null=True)
    diluted_eps = FloatField(default=0, blank=True, null=True)
    diluted_ni_availto_com_stockholders = FloatField(default=0, blank=True, null=True)
    ebit = FloatField(default=0, blank=True, null=True)
    ebitda = FloatField(default=0, blank=True, null=True)
    gross_profit = FloatField(default=0, blank=True, null=True)
    interest_expense = FloatField(default=0, blank=True, null=True)
    interest_expense_non_operating = FloatField(default=0, blank=True, null=True)
    interest_income = FloatField(default=0, blank=True, null=True)
    interest_income_non_operating = FloatField(default=0, blank=True, null=True)
    net_income = FloatField(default=0, blank=True, null=True)
    net_income_common_stockholders = FloatField(default=0, blank=True, null=True)
    net_income_continuous_operations = FloatField(default=0, blank=True, null=True)
    net_income_from_continuing_and_discontinued_operation = FloatField(default=0, blank=True, null=True)
    net_income_from_continuing_operation_net_minority_interest = FloatField(default=0, blank=True, null=True)
    net_income_including_noncontrolling_interests = FloatField(default=0, blank=True, null=True)
    net_interest_income = FloatField(default=0, blank=True, null=True)
    net_non_operating_interest_income_expense = FloatField(default=0, blank=True, null=True)
    normalized_ebitda = FloatField(default=0, blank=True, null=True)
    normalized_income = FloatField(default=0, blank=True, null=True)
    operating_expense = FloatField(default=0, blank=True, null=True)
    operating_income = FloatField(default=0, blank=True, null=True)
    operating_revenue = FloatField(default=0, blank=True, null=True)
    other_income_expense = FloatField(default=0, blank=True, null=True)
    other_non_operating_income_expenses = FloatField(default=0, blank=True, null=True)
    pretax_income = FloatField(default=0, blank=True, null=True)
    reconciled_cost_of_revenue = FloatField(default=0, blank=True, null=True)
    reconciled_depreciation = FloatField(default=0, blank=True, null=True)
    research_and_development = FloatField(default=0, blank=True, null=True)
    selling_general_and_administration = FloatField(default=0, blank=True, null=True)
    tax_effect_of_unusual_items = FloatField(default=0, blank=True, null=True)
    tax_provision = FloatField(default=0, blank=True, null=True)
    tax_rate_for_calcs = FloatField(default=0, blank=True, null=True)
    total_expenses = FloatField(default=0, blank=True, null=True)
    total_operating_income_as_reported = FloatField(default=0, blank=True, null=True)
    total_revenue = FloatField(default=0, blank=True, null=True)

    class Meta(BaseStatement.Meta):
        verbose_name = "Yahooquery Income Statement"
        verbose_name_plural = "Yahooquery Income Statements"
        db_table = "assets_companies_income_statements_yahooquery"

    def __str__(self):
        return self.company.ticker + str(self.date)


class BalanceSheetYahooQuery(BaseUnknownField):
    as_of_date = DateTimeField(blank=True, null=True)
    period_type = CharField(max_length=10, blank=True, null=True)
    currency_code = CharField(max_length=10, blank=True, null=True)
    accounts_payable = FloatField(default=0, blank=True, null=True)
    accounts_receivable = FloatField(default=0, blank=True, null=True)
    accumulated_depreciation = FloatField(default=0, blank=True, null=True)
    available_for_sale_securities = FloatField(default=0, blank=True, null=True)
    capital_stock = FloatField(default=0, blank=True, null=True)
    cash_and_cash_equivalents = FloatField(default=0, blank=True, null=True)
    cash_cash_equivalents_and_short_term_investments = FloatField(default=0, blank=True, null=True)
    cash_equivalents = FloatField(default=0, blank=True, null=True)
    cash_financial = FloatField(default=0, blank=True, null=True)
    commercial_paper = FloatField(default=0, blank=True, null=True)
    common_stock = FloatField(default=0, blank=True, null=True)
    common_stock_equity = FloatField(default=0, blank=True, null=True)
    current_assets = FloatField(default=0, blank=True, null=True)
    current_debt = FloatField(default=0, blank=True, null=True)
    current_debt_and_capital_lease_obligation = FloatField(default=0, blank=True, null=True)
    current_deferred_liabilities = FloatField(default=0, blank=True, null=True)
    current_deferred_revenue = FloatField(default=0, blank=True, null=True)
    current_liabilities = FloatField(default=0, blank=True, null=True)
    gains_losses_not_affecting_retained_earnings = FloatField(default=0, blank=True, null=True)
    gross_ppe = FloatField(default=0, blank=True, null=True)
    inventory = FloatField(default=0, blank=True, null=True)
    invested_capital = FloatField(default=0, blank=True, null=True)
    investmentin_financial_assets = FloatField(default=0, blank=True, null=True)
    investments_and_advances = FloatField(default=0, blank=True, null=True)
    land_and_improvements = FloatField(default=0, blank=True, null=True)
    leases = FloatField(default=0, blank=True, null=True)
    long_term_debt = FloatField(default=0, blank=True, null=True)
    long_term_debt_and_capital_lease_obligation = FloatField(default=0, blank=True, null=True)
    machinery_furniture_equipment = FloatField(default=0, blank=True, null=True)
    net_debt = FloatField(default=0, blank=True, null=True)
    net_ppe = FloatField(default=0, blank=True, null=True)
    net_tangible_assets = FloatField(default=0, blank=True, null=True)
    non_current_deferred_liabilities = FloatField(default=0, blank=True, null=True)
    non_current_deferred_revenue = FloatField(default=0, blank=True, null=True)
    non_current_deferred_taxes_liabilities = FloatField(default=0, blank=True, null=True)
    ordinary_shares_number = FloatField(default=0, blank=True, null=True)
    other_current_assets = FloatField(default=0, blank=True, null=True)
    other_current_borrowings = FloatField(default=0, blank=True, null=True)
    other_current_liabilities = FloatField(default=0, blank=True, null=True)
    other_non_current_assets = FloatField(default=0, blank=True, null=True)
    other_non_current_liabilities = FloatField(default=0, blank=True, null=True)
    other_receivables = FloatField(default=0, blank=True, null=True)
    other_short_term_investments = FloatField(default=0, blank=True, null=True)
    payables = FloatField(default=0, blank=True, null=True)
    payables_and_accrued_expenses = FloatField(default=0, blank=True, null=True)
    properties = FloatField(default=0, blank=True, null=True)
    receivables = FloatField(default=0, blank=True, null=True)
    retained_earnings = FloatField(default=0, blank=True, null=True)
    share_issued = FloatField(default=0, blank=True, null=True)
    stockholders_equity = FloatField(default=0, blank=True, null=True)
    tangible_book_value = FloatField(default=0, blank=True, null=True)
    total_assets = FloatField(default=0, blank=True, null=True)
    total_capitalization = FloatField(default=0, blank=True, null=True)
    total_debt = FloatField(default=0, blank=True, null=True)
    total_equity_gross_minority_interest = FloatField(default=0, blank=True, null=True)
    total_liabilities_net_minority_interest = FloatField(default=0, blank=True, null=True)
    total_non_current_assets = FloatField(default=0, blank=True, null=True)
    total_non_current_liabilities_net_minority_interest = FloatField(default=0, blank=True, null=True)
    tradeand_other_payables_non_current = FloatField(default=0, blank=True, null=True)
    working_capital = FloatField(default=0, blank=True, null=True)

    class Meta(BaseStatement.Meta):
        verbose_name = "Yahooquery Balance Sheet"
        verbose_name_plural = "Yahooquery Balance Sheets"
        db_table = "assets_companies_balance_sheet_statements_yahooquery"

    def __str__(self):
        return self.company.ticker + str(self.date)


class CashflowStatementYahooQuery(BaseUnknownField):
    as_of_date = DateTimeField(blank=True, null=True)
    period_type = CharField(max_length=10, blank=True, null=True)
    currency_code = CharField(max_length=10, blank=True, null=True)
    beginning_cash_position = FloatField(default=0, blank=True, null=True)
    capital_expenditure = FloatField(default=0, blank=True, null=True)
    cash_dividends_paid = FloatField(default=0, blank=True, null=True)
    cash_flow_from_continuing_financing_activities = FloatField(default=0, blank=True, null=True)
    cash_flow_from_continuing_investing_activities = FloatField(default=0, blank=True, null=True)
    cash_flow_from_continuing_operating_activities = FloatField(default=0, blank=True, null=True)
    change_in_account_payable = FloatField(default=0, blank=True, null=True)
    change_in_cash_supplemental_as_reported = FloatField(default=0, blank=True, null=True)
    change_in_inventory = FloatField(default=0, blank=True, null=True)
    change_in_other_current_assets = FloatField(default=0, blank=True, null=True)
    change_in_other_current_liabilities = FloatField(default=0, blank=True, null=True)
    change_in_other_working_capital = FloatField(default=0, blank=True, null=True)
    change_in_payable = FloatField(default=0, blank=True, null=True)
    change_in_payables_and_accrued_expense = FloatField(default=0, blank=True, null=True)
    change_in_receivables = FloatField(default=0, blank=True, null=True)
    change_in_working_capital = FloatField(default=0, blank=True, null=True)
    changes_in_account_receivables = FloatField(default=0, blank=True, null=True)
    changes_in_cash = FloatField(default=0, blank=True, null=True)
    common_stock_dividend_paid = FloatField(default=0, blank=True, null=True)
    common_stock_issuance = FloatField(default=0, blank=True, null=True)
    common_stock_payments = FloatField(default=0, blank=True, null=True)
    deferred_income_tax = FloatField(default=0, blank=True, null=True)
    deferred_tax = FloatField(default=0, blank=True, null=True)
    depreciation_amortization_depletion = FloatField(default=0, blank=True, null=True)
    depreciation_and_amortization = FloatField(default=0, blank=True, null=True)
    end_cash_position = FloatField(default=0, blank=True, null=True)
    financing_cash_flow = FloatField(default=0, blank=True, null=True)
    free_cash_flow = FloatField(default=0, blank=True, null=True)
    income_tax_paid_supplemental_data = FloatField(default=0, blank=True, null=True)
    interest_paid_supplemental_data = FloatField(default=0, blank=True, null=True)
    investing_cash_flow = FloatField(default=0, blank=True, null=True)
    issuance_of_capital_stock = FloatField(default=0, blank=True, null=True)
    issuance_of_debt = FloatField(default=0, blank=True, null=True)
    long_term_debt_issuance = FloatField(default=0, blank=True, null=True)
    long_term_debt_payments = FloatField(default=0, blank=True, null=True)
    net_business_purchase_and_sale = FloatField(default=0, blank=True, null=True)
    net_common_stock_issuance = FloatField(default=0, blank=True, null=True)
    net_income = FloatField(default=0, blank=True, null=True)
    net_income_from_continuing_operations = FloatField(default=0, blank=True, null=True)
    net_investment_purchase_and_sale = FloatField(default=0, blank=True, null=True)
    net_issuance_payments_of_debt = FloatField(default=0, blank=True, null=True)
    net_long_term_debt_issuance = FloatField(default=0, blank=True, null=True)
    net_other_financing_charges = FloatField(default=0, blank=True, null=True)
    net_other_investing_changes = FloatField(default=0, blank=True, null=True)
    net_ppe_purchase_and_sale = FloatField(default=0, blank=True, null=True)
    net_short_term_debt_issuance = FloatField(default=0, blank=True, null=True)
    operating_cash_flow = FloatField(default=0, blank=True, null=True)
    other_non_cash_items = FloatField(default=0, blank=True, null=True)
    purchase_of_business = FloatField(default=0, blank=True, null=True)
    purchase_of_investment = FloatField(default=0, blank=True, null=True)
    purchase_of_ppe = FloatField(default=0, blank=True, null=True)
    repayment_of_debt = FloatField(default=0, blank=True, null=True)
    repurchase_of_capital_stock = FloatField(default=0, blank=True, null=True)
    sale_of_investment = FloatField(default=0, blank=True, null=True)
    short_term_debt_payments = FloatField(default=0, blank=True, null=True)
    stock_based_compensation = FloatField(default=0, blank=True, null=True)

    class Meta(BaseStatement.Meta):
        verbose_name = "Yahooquery Cash flow Statement"
        verbose_name_plural = "Yahooquery Cash flow Statements"
        db_table = "assets_companies_cashflow_statements_yahooquery"

    def __str__(self):
        return self.company.ticker + str(self.date)


class KeyStatsYahooQuery(BaseUnknownField):
    period = None
    reported_currency = None
    max_age = FloatField(default=0, blank=True, null=True)
    price_hint = FloatField(default=0, blank=True, null=True)
    enterprise_value = FloatField(default=0, blank=True, null=True)
    forward_pe = FloatField(default=0, blank=True, null=True)
    profit_margins = FloatField(default=0, blank=True, null=True)
    float_shares = FloatField(default=0, blank=True, null=True)
    shares_outstanding = FloatField(default=0, blank=True, null=True)
    shares_short = FloatField(default=0, blank=True, null=True)
    shares_short_prior_month = FloatField(default=0, blank=True, null=True)
    shares_short_previous_month_date = DateTimeField(blank=True, null=True)
    date_short_interest = DateTimeField(blank=True, null=True)
    shares_percent_shares_out = FloatField(default=0, blank=True, null=True)
    held_percent_insiders = FloatField(default=0, blank=True, null=True)
    held_percent_institutions = FloatField(default=0, blank=True, null=True)
    short_ratio = FloatField(default=0, blank=True, null=True)
    short_percent_of_float = FloatField(default=0, blank=True, null=True)
    beta = FloatField(default=0, blank=True, null=True)
    category = FloatField(default=0, blank=True, null=True)
    book_value = FloatField(default=0, blank=True, null=True)
    price_to_book = FloatField(default=0, blank=True, null=True)
    fund_family = FloatField(default=0, blank=True, null=True)
    legal_type = FloatField(default=0, blank=True, null=True)
    last_fiscal_year_end = DateTimeField(blank=True, null=True)
    next_fiscal_year_end = DateTimeField(blank=True, null=True)
    most_recent_quarter = DateTimeField(blank=True, null=True)
    earnings_quarterly_growth = FloatField(default=0, blank=True, null=True)
    net_income_to_common = FloatField(default=0, blank=True, null=True)
    trailing_eps = FloatField(default=0, blank=True, null=True)
    forward_eps = FloatField(default=0, blank=True, null=True)
    peg_ratio = FloatField(default=0, blank=True, null=True)
    last_split_factor = CharField(max_length=10, blank=True, null=True)
    last_split_date = DateTimeField(blank=True, null=True)
    enterprise_to_revenue = FloatField(default=0, blank=True, null=True)
    enterprise_to_ebitda = FloatField(default=0, blank=True, null=True)
    week_change_52 = FloatField(default=0, blank=True, null=True)
    sand_p52_week_change = FloatField(default=0, blank=True, null=True)

    class Meta(BaseStatement.Meta):
        verbose_name = "Yahooquery Key stats"
        verbose_name_plural = "Yahooquery Key stats"
        db_table = "assets_companies_key stats_yahooquery"

    def __str__(self):
        return self.company.ticker + str(self.date)