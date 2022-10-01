import pytest
import datetime

from typing import Dict, Union, List
from bfet import DjangoTestingModel

from apps.socialmedias import constants as social_constants
from apps.web import constants as web_constants
from apps.api.models import Key
from apps.business.models import (
    Customer,
    Product,
    ProductComment,
    ProductComplementary,
    ProductComplementaryPaymentLink,
    ProductDiscount,
    ProductSubscriber,
    TransactionHistorial,
)
from apps.cartera.models import (
    Asset,
    FinancialObjectif,
    Income,
    Patrimonio,
    PositionMovement,
    Spend,
)
from apps.empresas.models import (
    Company,
    Exchange,
    ExchangeOrganisation,
    IncomeStatement,
    BalanceSheet,
    CashflowStatement,
)
from apps.escritos.models import (
    Term,
    TermContent,
    TermCorrection,
    TermsComment,
    TermsRelatedToResume,
)

# from apps.preguntas_respuestas.models import *
# from apps.public_blog.models import *
# from apps.web.models import WebsiteEmail, WebsiteEmailsType
# from apps.seo.models import *

# from apps.recsys.models import *
# from apps.screener.models import *
from apps.socialmedias.models import DefaultContent, DefaultTilte, Emoji

# from apps.super_investors.models import *
# from apps.roboadvisor.models import *
from apps.users.models import User
from apps.general.models import (
    Category,
    Country,
    Currency,
    EmailNotification,
    Industry,
    Notification,
    Sector,
    Tag,
    Period,
)

from tests.data import *
from apps.general import constants as general_constants

"""
function
--------
    Passing django_db_blocker as param avoids to use @pytest.mark.django_db
    and be allowed to use it for more than a function, otherwise use db

@pytest.fixture
---------------
    :param scope
        function:
            The default scope, the fixture is destroyed at the end of the test.

        class:
            The fixture is destroyed during the teardown of the last test in the class.

        module:
            The fixture is destroyed during teardown of the last test in the module.

        package:
            The fixture is destroyed during teardown of the last test in the package.

        session:
            The fixture is destroyed at the end of the test session.

TODO
Check if all fixtures are required to be used in session, class or maybe function is enought
"""

# General
@pytest.fixture(scope="session", autouse=True)
def currency(django_db_blocker) -> Currency:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Currency)


# Users
@pytest.fixture(scope="session", autouse=True)
def user_key_sub(django_db_blocker) -> User:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(User)


@pytest.fixture(scope="session", autouse=True)
def user_key(django_db_blocker) -> User:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(User)


@pytest.fixture(scope="session", autouse=True)
def user_key_removed(django_db_blocker) -> User:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(User)


# Business
@pytest.fixture(scope="session", autouse=True)
def customer(django_db_blocker, user_key_sub) -> Customer:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Customer, user=user_key_sub)


@pytest.fixture(scope="session", autouse=True)
def product(django_db_blocker) -> Product:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Product, title="Excel", slug="excel", is_active=True)


@pytest.fixture(scope="session", autouse=True)
def product_complementary(django_db_blocker, product, currency) -> ProductComplementary:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            ProductComplementary, title="Subscripción excel", product=product, is_active=True, currency=currency
        )


@pytest.fixture(scope="session", autouse=True)
def product_subscriber(django_db_blocker, product, product_complementary, user_key_sub) -> ProductSubscriber:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            ProductSubscriber,
            product=product,
            product_complementary=product_complementary,
            subscriber=user_key_sub,
            is_active=True,
        )


# Api
@pytest.fixture(scope="session", autouse=True)
def key(django_db_blocker, user_key) -> Key:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Key, user=user_key, in_use=True, removed=None)


@pytest.fixture(scope="session", autouse=True)
def subscription_key(django_db_blocker, user_key_sub, product_subscriber) -> Key:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            Key, user=user_key_sub, in_use=True, removed=None, subscription=product_subscriber
        )


@pytest.fixture(scope="session", autouse=True)
def removed_key(django_db_blocker, user_key_removed) -> Key:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Key, user=user_key_removed, in_use=False, removed=datetime.datetime.utcnow())


# Empresas
@pytest.fixture(scope="class")
def sector(django_db_blocker) -> Sector:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Sector)


@pytest.fixture(scope="class")
def industry(django_db_blocker) -> Industry:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Industry)


@pytest.fixture(scope="class")
def exchange_org_fr(django_db_blocker) -> ExchangeOrganisation:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(ExchangeOrganisation, name="France")


@pytest.fixture(scope="class")
def exchange_org_usa(django_db_blocker) -> ExchangeOrganisation:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(ExchangeOrganisation, name="Estados Unidos")


@pytest.fixture(scope="class")
def exchange_nyse(django_db_blocker, exchange_org_usa) -> Exchange:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Exchange, exchange_ticker="NYSE", main_org=exchange_org_usa)


@pytest.fixture(scope="class")
def exchange_euro(django_db_blocker, exchange_org_fr) -> Exchange:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Exchange, exchange_ticker="EURO", main_org=exchange_org_fr)


@pytest.fixture(scope="class")
def apple(django_db_blocker, sector, industry, exchange_nyse) -> Company:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            Company,
            ticker="AAPL",
            no_incs=False,
            no_bs=False,
            no_cfs=False,
            sector=sector,
            industry=industry,
            description_translated=True,
            updated=False,
            has_error=True,
            exchange=exchange_nyse,
            checkings={"has_institutionals": {"state": "no", "time": ""}},
        )


@pytest.fixture(scope="class")
def zinga(django_db_blocker, sector, industry, exchange_nyse) -> Company:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            Company,
            ticker="ZNGA",
            no_incs=False,
            no_bs=False,
            no_cfs=False,
            sector=sector,
            industry=industry,
            description_translated=False,
            updated=True,
            has_error=False,
            exchange=exchange_nyse,
            checkings={"has_institutionals": {"state": "yes", "time": ""}},
        )


@pytest.fixture(scope="class")
def louis(django_db_blocker, industry, exchange_euro) -> Company:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            Company,
            ticker="LVMH",
            no_incs=True,
            no_bs=False,
            no_cfs=False,
            industry=industry,
            description_translated=False,
            exchange=exchange_euro,
            updated=False,
            has_error=False,
            checkings={"has_institutionals": {"state": "no", "time": ""}},
        )


@pytest.fixture(scope="class")
def google(django_db_blocker, sector, industry, exchange_nyse) -> Company:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            Company,
            ticker="GOOGL",
            no_incs=False,
            no_bs=False,
            no_cfs=False,
            sector=sector,
            industry=industry,
            description_translated=True,
            exchange=exchange_nyse,
            updated=False,
            has_error=False,
            checkings={"has_institutionals": {"state": "no", "time": ""}},
        )


@pytest.fixture(scope="class")
def empresas_manager_companies(django_db_blocker, request, google, apple, zinga, louis, sector, industry) -> None:
    with django_db_blocker.unblock():
        request.cls.google = google
        request.cls.apple = apple
        request.cls.zinga = zinga
        request.cls.louis = louis
        request.cls.sector = sector
        request.cls.industry = industry
        yield


@pytest.fixture()
def clean_company(django_db_blocker) -> Company:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            Company,
            name="Intel",
            ticker="INTC",
            no_incs=False,
            no_bs=False,
            no_cfs=False,
            description_translated=True,
            has_logo=True,
            has_error=False,
        )


@pytest.fixture()
def period_for_year(django_db_blocker) -> Period:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(Period, year=2022, period=general_constants.PERIOD_FOR_YEAR)


@pytest.fixture(scope="session")
def yearly_income_statement(django_db_blocker, clean_company, period_for_year) -> IncomeStatement:
    """
    Company: Intel (INTC)
    Period: For year (2022)
    """
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(IncomeStatement, is_ttm=False, compny=clean_company, period=period_for_year)


@pytest.fixture(scope="session")
def yearly_balance_sheet(django_db_blocker, clean_company, period_for_year) -> BalanceSheet:
    """
    Company: Intel (INTC)
    Period: For year (2022)
    """
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(BalanceSheet, is_ttm=False, compny=clean_company, period=period_for_year)


@pytest.fixture(scope="session")
def yearly_cashflow_statement(django_db_blocker, clean_company, period_for_year) -> CashflowStatement:
    """
    Company: Intel (INTC)
    Period: For year (2022)
    """
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(CashflowStatement, is_ttm=False, compny=clean_company, period=period_for_year)


# Web exclusive
@pytest.fixture
def web_filters() -> Dict[str, Union[int, str]]:
    return {"for_content": social_constants.WEB, "purpose": web_constants.CONTENT_FOR_ENGAGEMENT}


@pytest.fixture(scope="function")
def web_title(django_db_blocker, web_filters) -> DefaultTilte:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(DefaultTilte, title=DjangoTestingModel.create_random_string(10), **web_filters)


@pytest.fixture(scope="function")
def web_content(django_db_blocker, web_filters) -> DefaultContent:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            DefaultContent, title=DjangoTestingModel.create_random_string(10), **web_filters
        )


@pytest.fixture(scope="function")
def web_emojis(django_db_blocker) -> Emoji:
    with django_db_blocker.unblock():
        return DjangoTestingModel.create(
            Emoji,
            2,
            emoji=DjangoTestingModel.create_random_string(10),
        )
