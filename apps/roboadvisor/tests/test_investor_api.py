from django.test import RequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from apps.empresas.tests.factories import CompanyFactory
from apps.users.tests.factories import UserFactory

from apps.roboadvisor.api.views import (
    RoboAdvisorQuestionCompanyAnalysisAPIView,
    RoboAdvisorQuestionFinancialSituationAPIView,
    RoboAdvisorQuestionInvestorExperienceAPIView,
    RoboAdvisorQuestionPortfolioAssetsWeightAPIView,
    RoboAdvisorQuestionPortfolioCompositionAPIView,
    RoboAdvisorQuestionRiskAversionAPIView,
    RoboAdvisorQuestionStocksPortfolioAPIView,
)
from apps.roboadvisor.views import RoboAdvisorResultView
from apps.roboadvisor.tests.factories import RoboAdvisorServiceFactory, RoboAdvisorServiceStepFactory


class TestInvoicesAllAPI(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.company = CompanyFactory()

    def test_roboadvisor_question_company_analysis_API_view(self, rf: RequestFactory):
        data = {}
        url = f'/robo-step-analysis'
        request = rf.post(url, data=data)

    def test_roboadvisor_question_financial_situation_API_view(self, rf: RequestFactory):
        data = {}
        url = f'/robo-step-financial'
        request = rf.post(url, data=data)

    def test_roboadvisor_question_investor_experience_API_view(self, rf: RequestFactory):
        data = {}
        url = f'/robo-step-experience'
        request = rf.post(url, data=data)

    def test_roboadvisor_question_portfolio_assets_weight_API_view(self, rf: RequestFactory):
        data = {}
        url = f'/robo-step-weights'
        request = rf.post(url, data=data)

    def test_roboadvisor_question_portfolio_composition_API_view(self, rf: RequestFactory):
        data = {}
        url = f'/robo-step-composition'
        request = rf.post(url, data=data)

    def test_roboadvisor_question_risk_aversion_API_view(self, rf: RequestFactory):
        data = {}
        url = f'/robo-step-risk-aversion'
        request = rf.post(url, data=data)

    def test_roboadvisor_question_stocks_portfolio_API_view(self, rf: RequestFactory):
        data = {}
        url = f'/robo-step-stocks-portfolio'
        request = rf.post(url, data=data)

    def test_roboadvisor_result(self):
        slug = ''
        url = f'/robo-result/{slug}/'
