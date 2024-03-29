from typing import Callable, Type, Union

import pandas as pd

from src.periods.models import Period


class DFInfoCreator:
    period_quarter = Period.objects.first_quarter_period
    period_year = Period.objects.for_year_period
    income_statement_model = None
    balance_sheet_model = None
    cashflow_statement_model = None
    normalize_income_statement = None
    normalize_balance_sheet = None
    normalize_cashflow_statement = None

    def create_financials(
        self,
        incomes_df: pd.DataFrame,
        balance_sheets_df: pd.DataFrame,
        cashflows_df: pd.DataFrame,
        period: Union[Period.objects.first_quarter_period, Period.objects.for_year_period],
    ):
        self.create_statement(
            incomes_df,
            period,
            self.normalize_income_statement,
            self.income_statement_model,
        )
        self.create_statement(
            balance_sheets_df,
            period,
            self.normalize_balance_sheet,
            self.balance_sheet_model,
        )
        self.create_statement(
            cashflows_df,
            period,
            self.normalize_cashflow_statement,
            self.cashflow_statement_model,
        )

    def create_statement(
        self,
        df: pd.DataFrame,
        period: Callable,
        normalizer: Callable,
        model: Type,
    ):
        df = df.fillna(0)
        self.create_statements_from_df(df, period, normalizer, model)

    def create_statements_from_df(
        self,
        df: pd.DataFrame,
        period: Callable,
        normalizer: Callable,
        model: Type,
    ):
        raise NotImplementedError
