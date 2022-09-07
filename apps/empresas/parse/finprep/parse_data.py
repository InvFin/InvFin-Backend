from typing import List, Dict
import time
import random

from django.conf import settings

from apps.general.outils.parser_client import ParserClient
from apps.empresas import constants


class ParseFinprep(ParserClient):
    base_path = constants.FINPREP_BASE_URL
    api_version = "v3"
    auth = {"apikey": settings.FINPREP_KEY}

    def request_income_statements_finprep(
        self,
        ticker,
        dict_params: Dict[str, str] = {"limit": 120}
    ) -> List:
        return self.request(
            path="income-statement",
            str_params=ticker,
            dict_params=dict_params
        )

    def request_balance_sheets_finprep(
        self,
        ticker,
        dict_params: Dict[str, str] = {"limit": 120}
    ) -> List:
        return self.request(
            path="balance-sheet-statement",
            str_params=ticker,
            dict_params=dict_params
        )

    def request_cashflow_statements_finprep(
        self,
        ticker,
        dict_params: Dict[str, str] = {"limit": 120}
    ) -> List:
        return self.request(
            path="cash-flow-statement",
            str_params=ticker,
            dict_params=dict_params
        )

    def request_financials_finprep(
        self,
        ticker,
        dict_params: Dict[str, str] = {"limit": 120}
    ) -> Dict[str, List]:
        random_int = random.randint(5, 10)
        income_statements = self.request_income_statements_finprep(
            ticker,
            dict_params=dict_params
        )
        time.sleep(random_int)
        balance_sheets = self.request_balance_sheets_finprep(
            ticker,
            dict_params=dict_params
        )
        time.sleep(random_int)
        cashflow_statements = self.request_cashflow_statements_finprep(
            ticker,
            dict_params=dict_params
        )
        return {
            "income_statements": income_statements,
            "balance_sheets": balance_sheets,
            "cashflow_statements": cashflow_statements,
        }