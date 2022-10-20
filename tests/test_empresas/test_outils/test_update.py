from django.test import TestCase

from bfet import DjangoTestingModel, DataCreator

from apps.general import constants
from apps.general.models import Period, Currency
from apps.empresas.outils.update import UpdateCompany
from apps.empresas.models import (
    Company,
    IncomeStatementYahooQuery,
    IncomeStatementYFinance,
    IncomeStatementFinprep,
    BalanceSheetYahooQuery,
    BalanceSheetYFinance,
    BalanceSheetFinprep,
    CashflowStatementYahooQuery,
    CashflowStatementYFinance,
    CashflowStatementFinprep,
    IncomeStatement,
    BalanceSheet,
    CashflowStatement,
)


class TestUpdateCompany(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = DjangoTestingModel.create(Company, ticker="INTC", name="Intel")
        cls.period = DjangoTestingModel.create(Period, year=2021, period=constants.PERIOD_FOR_YEAR)
        cls.currency = DjangoTestingModel.create(Currency)
        cls.revenue = DataCreator.create_random_float()
        cls.cost_of_revenue = DataCreator.create_random_float()
        cls.gross_profit = DataCreator.create_random_float()
        cls.research_and_development_expenses = DataCreator.create_random_float()
        cls.selling_general_and_administrative_expenses = DataCreator.create_random_float()
        cls.inc_st_finprep = DjangoTestingModel.create(
            IncomeStatementFinprep,
            reported_currency=cls.currency,
            company=cls.company,
            period=cls.period,
            revenue=cls.revenue,
            cost_of_revenue=cls.cost_of_revenue,
            gross_profit=cls.gross_profit,
            research_and_development_expenses=cls.research_and_development_expenses,
            selling_general_and_administrative_expenses=cls.selling_general_and_administrative_expenses,
        )
        cls.inc_st_yahooquery = DjangoTestingModel.create(
            IncomeStatementYahooQuery,
            reported_currency=cls.currency,
            company=cls.company,
            period=cls.period,
            total_revenue=cls.revenue,
            reconciled_cost_of_revenue=cls.cost_of_revenue,
            gross_profit=cls.gross_profit,
            research_and_development=cls.research_and_development_expenses,
            selling_general_and_administration=cls.selling_general_and_administrative_expenses,
        )
        cls.inc_st_yfinance = DjangoTestingModel.create(
            IncomeStatementYFinance,
            reported_currency=cls.currency,
            company=cls.company,
            period=cls.period,
            total_revenue=cls.revenue,
            cost_of_revenue=cls.cost_of_revenue,
            gross_profit=cls.gross_profit,
            research_development=cls.research_and_development_expenses,
            selling_general_administrative=cls.selling_general_and_administrative_expenses,
        )
        cls.bs_finprep = DjangoTestingModel.create(BalanceSheetFinprep, company=cls.company, period=cls.period)
        cls.bs_yahooquery = DjangoTestingModel.create(BalanceSheetYahooQuery, company=cls.company, period=cls.period)
        cls.bs_yfinance = DjangoTestingModel.create(BalanceSheetYFinance, company=cls.company, period=cls.period)
        cls.cf_st_finprep = DjangoTestingModel.create(CashflowStatementFinprep, company=cls.company, period=cls.period)
        cls.cf_st_yahooquery = DjangoTestingModel.create(
            CashflowStatementYahooQuery, company=cls.company, period=cls.period
        )
        cls.cf_st_yfinance = DjangoTestingModel.create(
            CashflowStatementYFinance, company=cls.company, period=cls.period
        )

    def test_update_average_financials_statements(self):
        assert 0 == IncomeStatement.objects.all().count()
        assert 0 == BalanceSheet.objects.all().count()
        assert 0 == CashflowStatement.objects.all().count()
        UpdateCompany(self.company).update_average_financials_statements(self.period)
        assert 1 == IncomeStatement.objects.all().count()
        assert 1 == BalanceSheet.objects.all().count()
        assert 1 == CashflowStatement.objects.all().count()

    def test_create_ttm(self):
        assert 0 == IncomeStatement.objects.filter(is_ttm=True).count()
        assert 0 == BalanceSheet.objects.filter(is_ttm=True).count()
        assert 0 == CashflowStatement.objects.filter(is_ttm=True).count()
        periods = [
            DjangoTestingModel.create(Period, year=2021, period=constants.PERIOD_2_QUARTER),
            DjangoTestingModel.create(Period, year=2021, period=constants.PERIOD_3_QUARTER),
            DjangoTestingModel.create(Period, year=2021, period=constants.PERIOD_4_QUARTER),
            DjangoTestingModel.create(Period, year=2022, period=constants.PERIOD_1_QUARTER),
        ]
        for period in periods:
            DjangoTestingModel.create(
                IncomeStatement, company=self.company, period=period, date=period.year, is_ttm=False
            )
            DjangoTestingModel.create(BalanceSheet, company=self.company, period=period, date=period.year, is_ttm=False)
            DjangoTestingModel.create(
                CashflowStatement, company=self.company, period=period, date=period.year, is_ttm=False
            )

        UpdateCompany(self.company).create_or_update_ttm()
        assert 1 == IncomeStatement.objects.filter(is_ttm=True).count()
        assert 1 == BalanceSheet.objects.filter(is_ttm=True).count()
        assert 1 == CashflowStatement.objects.filter(is_ttm=True).count()

        income_statement = IncomeStatement.objects.filter(is_ttm=True).first()
        balance_sheet = BalanceSheet.objects.filter(is_ttm=True).first()
        cashflow_statement = CashflowStatement.objects.filter(is_ttm=True).first()
        assert 2022 == income_statement.year
        assert 2022 == balance_sheet.year
        assert 2022 == cashflow_statement.year
