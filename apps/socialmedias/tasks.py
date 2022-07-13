import random

from apps.empresas.company.update import UpdateCompany
from apps.empresas.models import Company
from apps.escritos.models import Term
from apps.preguntas_respuestas.models import Question
from apps.public_blog.models import PublicBlog, WritterProfile
from config import celery_app

from .models import (
    BlogSharedHistorial,
    CompanySharedHistorial,
    NewsSharedHistorial,
    ProfileSharedHistorial,
    QuestionSharedHistorial,
    TermSharedHistorial,
)
from .poster import SocialPosting


@celery_app.task()
def socialmedia_share_company():
    post_type = 6
    content_shared = Company.objects.random_complete_companies_by_main_exchange('Estados Unidos')
    if content_shared.has_meta_image is False:
        UpdateCompany(content_shared).save_logo_remotely()
    SocialPosting(CompanySharedHistorial, content_shared=content_shared).share_content(post_type)


@celery_app.task()
def socialmedia_share_news():
    post_type = 6
    market = random.choice(['Estados Unidos', 'México'])
    company_related = Company.objects.random_complete_companies_by_main_exchange(market)
    if company_related.has_meta_image is False:
        UpdateCompany(company_related).save_logo_remotely()
    SocialPosting(NewsSharedHistorial, company_related=company_related).share_content(post_type)


@celery_app.task()
def socialmedia_share_term():
    post_type = 6
    content_shared = Term.objects.get_random()
    SocialPosting(TermSharedHistorial, content_shared=content_shared).share_content(post_type)


@celery_app.task()
def socialmedia_share_blog():
    post_type = 6
    content_shared = PublicBlog.objects.get_random()
    SocialPosting(BlogSharedHistorial, content_shared=content_shared).share_content(post_type)


@celery_app.task()
def socialmedia_share_question():
    post_type = 3
    content_shared = Question.objects.get_random()
    SocialPosting(QuestionSharedHistorial, content_shared=content_shared).share_content(post_type)

