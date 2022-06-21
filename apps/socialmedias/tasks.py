import random

from config import celery_app

from apps.escritos.models import Term
from apps.preguntas_respuestas.models import Question
from apps.public_blog.models import PublicBlog, WritterProfile
from apps.empresas.models import Company
from apps.empresas.company.update import UpdateCompany

from .poster import SocialPosting
from .models import (
    CompanySharedHistorial,
    BlogSharedHistorial,
    NewsSharedHistorial,
    TermSharedHistorial,
    ProfileSharedHistorial,
    QuestionSharedHistorial
)

@celery_app.task()
def socialmedia_share_company():
    post_type = 6
    content_shared = Company.objects.random_complete_companies_by_main_exchange('Estados Unidos')
    SocialPosting(CompanySharedHistorial, content_shared=content_shared).share_content(post_type)


@celery_app.task()
def socialmedia_share_news():
    post_type = 6
    market = random.choice(['Estados Unidos', 'México'])
    company_related = Company.objects.random_complete_companies_by_main_exchange(market)
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

