from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q

from config import celery_app

from apps.empresas.company.update import UpdateCompany
from apps.empresas.company.retrieve_data import RetrieveCompanyData
from apps.empresas.models import Company


@celery_app.task()
def update_basic_info_company_task():
    companies_without_info = Company.objects.filter(Q(has_logo=False) | Q(description_translated=False))
    if companies_without_info.exists():
        company = companies_without_info.first()
        return UpdateCompany(company).general_update()
    else:
        return send_mail('No companies left', 'All companies have info', settings.EMAIL_DEFAULT, [settings.EMAIL_DEFAULT])


@celery_app.task()
def update_company_key_stats_task():
    companies_without_info = Company.objects.filter_checkings_not_seen("key_stats")
    if companies_without_info.exists():
        company = companies_without_info.first()
        return RetrieveCompanyData(company).create_key_stats_yahooquery()
    else:
        return send_mail(
            'No companies left to update key_stats',
            f'All companies have info for key_stats',
            settings.EMAIL_DEFAULT,
            [settings.EMAIL_DEFAULT]
        )


@celery_app.task()
def update_company_institutionals_task():
    companies_without_info = Company.objects.filter_checkings_not_seen("institutionals")
    if companies_without_info.exists():
        company = companies_without_info.first()
        return RetrieveCompanyData(company).create_institutionals_yahooquery()
    else:
        return send_mail(
            'No companies left to update institutionals',
            f'All companies have info for institutionals',
            settings.EMAIL_DEFAULT,
            [settings.EMAIL_DEFAULT]
        )


@celery_app.task()
def update_company_financials_finprep_task():
    companies_without_info = Company.objects.filter_checkings_not_seen("latest_financials_finprep_info")
    if companies_without_info.exists():
        company = companies_without_info.first()
        return RetrieveCompanyData(company).create_financials_finprep()
    else:
        return send_mail(
            'No companies left to update financials for latest_financials_finprep_info',
            f'All companies have info for latest_financials_finprep_info',
            settings.EMAIL_DEFAULT,
            [settings.EMAIL_DEFAULT]
        )


@celery_app.task()
def update_company_financials_finnhub_task():
    companies_without_info = Company.objects.filter_checkings_not_seen("first_financials_finnhub_info")
    if companies_without_info.exists():
        company = companies_without_info.first()
        return RetrieveCompanyData(company).create_financials_finnhub()
    else:
        return send_mail(
            'No companies left to update financials first_financials_finnhub_info',
            f'All companies have info for first_financials_finnhub_info',
            settings.EMAIL_DEFAULT,
            [settings.EMAIL_DEFAULT]
        )


@celery_app.task()
def update_company_financials_yfinance_task():
    companies_without_info = Company.objects.filter_checkings_not_seen("first_financials_yfinance_info")
    if companies_without_info.exists():
        company = companies_without_info.first()
        RetrieveCompanyData(company).create_financials_yfinance("a")
        RetrieveCompanyData(company).create_financials_yfinance("q")
    else:
        return send_mail(
            'No companies left to update financials for first_financials_yfinance_info',
            f'All companies have info for first_financials_yfinance_info',
            settings.EMAIL_DEFAULT,
            [settings.EMAIL_DEFAULT]
        )


@celery_app.task()
def update_company_financials_yahooquery_task():
    companies_without_info = Company.objects.filter_checkings_not_seen("first_financials_yahooquery_info")
    if companies_without_info.exists():
        company = companies_without_info.first()
        RetrieveCompanyData(company).create_financials_yahooquery("a")
        RetrieveCompanyData(company).create_financials_yahooquery("q")
    else:
        return send_mail(
            'No companies left to update financials ofr first_financials_yahooquery_info',
            f'All companies have info for first_financials_yahooquery_info',
            settings.EMAIL_DEFAULT,
            [settings.EMAIL_DEFAULT]
        )
