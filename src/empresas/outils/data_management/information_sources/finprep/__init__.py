from typing import Callable, Dict, List, Optional, Type, Union, Any

from src.empresas.models import (
    BalanceSheetFinprep,
    CashflowStatementFinprep,
    IncomeStatementFinprep,
)
from .normalize_data import NormalizeFinprep
from .parse_data import ParseFinprep


class FinprepInfo(NormalizeFinprep, ParseFinprep):
    def __init__(self, company) -> None:
        self.company = company

    def create_statement_finprep(
        self,
        list_statements_finprep: List,
        statement_model: Union[
            Type[BalanceSheetFinprep],
            Type[IncomeStatementFinprep],
            Type[CashflowStatementFinprep],
        ],
        normalize_data: Callable,
    ) -> List:
        data_saved = []
        for statements_finprep in list_statements_finprep:
            statement_data = normalize_data(statements_finprep)
            obj, created = statement_model.objects.update_or_create(
                company=statement_data.pop("company"),
                period=statement_data.pop("period"),
                defaults=statement_data,
            )
            data_saved.append(obj)
        return data_saved

    def create_income_statements_finprep(
        self,
        list_income_statements_finprep: Optional[List] = None,
    ) -> List:
        if not list_income_statements_finprep:
            list_income_statements_finprep = self.request_income_statements_finprep(
                self.company.ticker
            )
        return self.create_statement_finprep(
            list_income_statements_finprep,
            IncomeStatementFinprep,
            self.normalize_income_statements_finprep,
        )

    def create_balance_sheets_finprep(
        self,
        list_balance_sheets_finprep: Optional[List] = None,
    ) -> List:
        if not list_balance_sheets_finprep:
            list_balance_sheets_finprep = self.request_balance_sheets_finprep(
                self.company.ticker
            )
        return self.create_statement_finprep(
            list_balance_sheets_finprep,
            BalanceSheetFinprep,
            self.normalize_balance_sheets_finprep,
        )

    def create_cashflow_statements_finprep(
        self,
        list_cashflow_statements_finprep: Optional[List] = None,
    ) -> List:
        if not list_cashflow_statements_finprep:
            list_cashflow_statements_finprep = self.request_cashflow_statements_finprep(
                self.company.ticker
            )
        return self.create_statement_finprep(
            list_cashflow_statements_finprep,
            CashflowStatementFinprep,
            self.normalize_cashflow_statements_finprep,
        )

    def create_financials_finprep(self) -> Dict[str, Any]:
        financials_finprep = self.request_financials_finprep(self.company.ticker)
        return {
            key: value(financials_finprep[key])
            for key, value in {
                "income_statements": self.create_income_statements_finprep,
                "balance_sheets": self.create_balance_sheets_finprep,
                "cashflow_statements": self.create_cashflow_statements_finprep,
            }.items()
        }
