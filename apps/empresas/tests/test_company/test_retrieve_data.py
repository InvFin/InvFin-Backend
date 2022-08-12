import time
import vcr

from django.test import TestCase

from apps.empresas.company.update import UpdateCompany
from apps.empresas.company.retrieve_data import RetrieveCompanyData

from apps.empresas.tests import finprep_data
from apps.empresas.tests.factories import CompanyFactory


company_vcr = vcr.VCR(
    cassette_library_dir='cassettes/company/retrieve/',
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
)


class TestRetrieveCompanyData(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.company = CompanyFactory()
        cls.company_update = UpdateCompany(cls.company)
        cls.company.inc_statements.create(date = 2018)
        cls.zinga = CompanyFactory(
            ticker='ZNGA'
        )



    @company_vcr.use_cassette()
    def test_get_current_price_not_found(self):
        comp_data = RetrieveCompanyData("ZNGA").get_current_price()

    @company_vcr.use_cassette()
    def test_get_current_price(self):
        comp_data = RetrieveCompanyData("AAPL").get_current_price()
