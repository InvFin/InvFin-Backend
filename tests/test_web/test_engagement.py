from django.test import TestCase
from django.contrib.auth import get_user_model

from unittest.mock import patch
from bfet import DjangoTestingModel

from apps.web import constants
from apps.socialmedias.outils.content_creation import (
    QuestionContentCreation,
    CompanyNewsContentCreation,
    TermContentCreation,
    PublicBlogContentCreation,
    CompanyContentCreation,
)
from apps.escritos.models import Term
from apps.web.outils.engagement import EngagementMachine
from apps.web.models import WebsiteEmail
from apps.socialmedias import constants as social_constants
from apps.socialmedias.models import Emoji, DefaultTilte


class TestEngagementMachine(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.defualt_title = DjangoTestingModel.create(
            DefaultTilte,
            title="Default title",
            for_content=social_constants.WEB,
        )
        cls.title_emojis = DjangoTestingModel.create(Emoji, emoji="emoji")
        cls.term = DjangoTestingModel.create(Term, title="term default")

    def test_get_creator(self):
        assert EngagementMachine().get_creator(social_constants.QUESTION_FOR_CONTENT) == QuestionContentCreation
        assert EngagementMachine().get_creator(social_constants.NEWS_FOR_CONTENT) == CompanyNewsContentCreation
        assert EngagementMachine().get_creator(social_constants.TERM_FOR_CONTENT) == TermContentCreation
        assert EngagementMachine().get_creator(social_constants.PUBLIC_BLOG_FOR_CONTENT) == PublicBlogContentCreation
        assert EngagementMachine().get_creator(social_constants.COMPANY_FOR_CONTENT) == CompanyContentCreation

    def test_send_website_email_engagement(self):
        title = "Default title"
        content = "Insider content"
        whom_to_send = constants.WHOM_TO_SEND_EMAIL_ALL
        newsletter_data = {
            "title": title,
            "content": content,
            "title_emojis": [self.title_emojis],
            "content": content,
            "whom_to_send": whom_to_send,
        }
        result_data = EngagementMachine().save_newsletter(**newsletter_data)
        assert isinstance(result_data, WebsiteEmail)
        assert title == result_data.title
        assert content == result_data.content
        assert (self.title_emojis in result_data.title_emojis.all()) is True
        assert whom_to_send == result_data.whom_to_send

    def test_create_newsletter(self):
        web_email_type = constants.CONTENT_FOR_ENGAGEMENT
        content_object = social_constants.TERM_FOR_CONTENT
        whom_to_send = constants.WHOM_TO_SEND_EMAIL_ALL

        web_email = EngagementMachine().create_newsletter(web_email_type, content_object, whom_to_send)
        assert isinstance(web_email, WebsiteEmail)
