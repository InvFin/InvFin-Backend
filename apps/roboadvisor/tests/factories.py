from factory import SubFactory
from factory.django import DjangoModelFactory

from ..models import (
    RoboAdvisorServiceStep,
    RoboAdvisorService,
    TemporaryInvestorProfile,
    InvestorProfile,

    RoboAdvisorQuestionInvestorExperience,
    RoboAdvisorQuestionCompanyAnalysis,
    RoboAdvisorQuestionFinancialSituation,
    RoboAdvisorQuestionRiskAversion,
    RoboAdvisorQuestionPortfolioAssetsWeight,
    RoboAdvisorQuestionStocksPortfolio,
    RoboAdvisorQuestionPortfolioComposition,

    RoboAdvisorUserServiceActivity,
    RoboAdvisorUserServiceStepActivity
)