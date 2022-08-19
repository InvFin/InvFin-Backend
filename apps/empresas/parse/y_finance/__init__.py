from typing import Type, Callable
import pandas as pd

from apps.general.outils.save_from_df import DFInfoCreator
from apps.empresas.models import BalanceSheetYFinance, CashflowStatementYFinance, IncomeStatementYFinance
from apps.empresas.parse.y_finance.normalize_data import NormalizeYFinance
from apps.empresas.parse.y_finance.parse_data import ParseYFinance


class YFinanceInfo(DFInfoCreator, NormalizeYFinance, ParseYFinance):
    income_statement_model = IncomeStatementYFinance
    balance_sheet_model = BalanceSheetYFinance
    cashflow_statement_model = CashflowStatementYFinance

    def __init__(self, company) -> None:
        super().__init__(company)
        self.company = company
        self.normalize_income_statement = self.normalize_income_statements_yfinance
        self.normalize_balance_sheet = self.normalize_balance_sheets_yfinance
        self.normalize_cashflow_statement = self.normalize_cashflow_statements_yfinance

    def create_statements_from_df(
        self,
        df: Type[pd.DataFrame],
        period: Callable,
        function: Callable,
        model: Type
    ):
        for column in df:
            model.objects.create(
                financials=df[column].to_dict(),
                # **function(df[column], column, period)
                **self.initial_data(column, period)
            )
        return

    def create_quarterly_financials_yfinance(self):
        self.create_financials(
            self.request_quarterly_financials_yfinance,
            self.request_quarterly_balance_sheet_yfinance,
            self.request_quarterly_cashflow_yfinance,
            self.period_quarter
        )

    def create_yearly_financials_yfinance(self):
        self.create_financials(
            self.request_financials_yfinance,
            self.request_balance_sheet_yfinance,
            self.request_cashflow_yfinance,
            self.period_year
        )
