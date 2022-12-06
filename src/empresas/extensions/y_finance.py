from .base_averages import AverageBalanceSheet, AverageCashflowStatement, AverageIncomeStatement


class IncomeStatementYFinanceExtended(AverageIncomeStatement):
    revenue_field = "total_revenue"
    cost_of_revenue_field = "cost_of_revenue"
    gross_profit_field = "gross_profit"
    rd_expenses_field = "research_development"
    general_administrative_expenses_field = ""
    selling_marketing_expenses_field = ""
    sga_expenses_field = "selling_general_administrative"
    other_expenses_field = ""
    operating_expenses_field = ""
    cost_and_expenses_field = "total_operating_expenses"
    interest_expense_field = ""
    depreciation_amortization_field = ""
    ebitda_field = ""
    operating_income_field = "operating_income"
    net_total_other_income_expenses_field = ""
    income_before_tax_field = "income_before_tax"
    income_tax_expenses_field = "income_tax_expense"
    net_income_field = "net_income_applicable_to_common_shares"
    weighted_average_shares_outstanding_field = ""
    weighted_average_diluated_shares_outstanding_field = ""


class BalanceSheetYFinanceExtended(AverageBalanceSheet):
    cash_and_cash_equivalents_field = "cash"
    short_term_investments_field = "short_term_investments"
    cash_and_short_term_investments_field = ""
    net_receivables_field = "net_receivables"
    inventory_field = "inventory"
    other_current_assets_field = "other_current_assets"
    total_current_assets_field = "total_current_assets"
    property_plant_equipment_field = ""
    goodwill_field = ""
    intangible_assets_field = ""
    goodwill_and_intangible_assets_field = ""
    long_term_investments_field = "long_term_investments"
    tax_assets_field = ""
    other_non_current_assets_field = ""
    total_non_current_assets_field = ""
    other_assets_field = ""
    total_assets_field = "total_assets"
    account_payables_field = "accounts_payable"
    short_term_debt_field = ""
    tax_payables_field = ""
    deferred_revenue_field = ""
    other_current_liabilities_field = ""
    total_current_liabilities_field = "total_current_liabilities"
    long_term_debt_field = "long_term_debt"
    deferred_revenue_non_current_field = ""
    deferred_tax_liabilities_non_current_field = ""
    other_non_current_liabilities_field = ""
    total_non_current_liabilities_field = ""
    other_liabilities_field = ""
    total_liabilities_field = "total_liab"
    common_stocks_field = "common_stock"
    retained_earnings_field = "retained_earnings"
    accumulated_other_comprehensive_income_loss_field = ""
    othertotal_stockholders_equity_field = ""
    total_stockholders_equity_field = "total_stockholder_equity"
    total_liabilities_and_total_equity_field = "total_assets"
    total_investments_field = ""
    total_debt_field = ""
    net_debt_field = ""


class CashflowStatementYFinanceExtended(AverageCashflowStatement):
    net_income_field = "net_income"
    depreciation_amortization_field = "depreciation"
    deferred_income_tax_field = ""
    stock_based_compesation_field = ""
    change_in_working_capital_field = ""
    accounts_receivables_field = "change_to_account_receivables"
    inventory_field = "change_to_inventory"
    accounts_payable_field = ""
    other_working_capital_field = ""
    other_non_cash_items_field = ""
    operating_activities_cf_field = ""
    investments_property_plant_equipment_field = ""
    acquisitions_net_field = ""
    purchases_investments_field = ""
    sales_maturities_investments_field = ""
    other_investing_activites_field = "other_cashflows_from_investing_activities"
    investing_activities_cf_field = ""
    debt_repayment_field = ""
    common_stock_issued_field = "issuance_of_stock"
    common_stock_repurchased_field = ""
    dividends_paid_field = "dividends_paid"
    other_financing_activities_field = ""
    financing_activities_cf_field = ""
    effect_forex_exchange_field = ""
    net_change_cash_field = ""
    cash_end_period_field = ""
    cash_beginning_period_field = ""
    operating_cf_field = ""
    capex_field = "capital_expenditures"
    fcf_field = ""