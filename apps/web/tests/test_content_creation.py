from apps.bfet import ExampleModel

from django.test import TestCase

from apps.web.outils.content_creation import WebsiteContentCreation
from apps.socialmedias.models import DefaultContent, DefaultTilte, Emoji
from apps.socialmedias import constants as social_constants
from apps.web import constants as web_constants
from apps.web.models import (
    WebsiteEmail,
    WebsiteEmailsType
)


class TestWebsiteContentCreation(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.filters = {
            "for_content": social_constants.WEB,
            "purpose": web_constants.CONTENT_FOR_ENGAGEMENT
        }
        cls.content = ExampleModel.create(DefaultContent, **cls.filters)
        cls.title = ExampleModel.create(
            DefaultTilte,
            title=ExampleModel.create_random_string(200),
            **cls.filters
        )
        cls.emojis = ExampleModel.create(
            Emoji,
            2,
            emoji=ExampleModel.create_random_string(10),
        )

    def test_create_title(self):
        custom_title = "Custom title"
        custom_dict = WebsiteContentCreation.create_title(custom_title)
        custom_expected_result = {"title": custom_title}
        self.assertEqual(custom_dict, custom_expected_result)

        default_dict = WebsiteContentCreation.create_title(filter=self.filters)
        default_expected_result = {
            "title": self.title.title,
            "default_title": self.title
        }
        self.assertEqual(default_dict, default_expected_result)

    def test_create_content(self):
        custom_content = "Custom custom_content"
        custom_dict = WebsiteContentCreation.create_content(custom_content)
        custom_expected_result = {"content": custom_content}
        self.assertEqual(custom_dict, custom_expected_result)

        default_dict = WebsiteContentCreation.create_content(filter=self.filters)
        default_expected_result = {
            "content": self.content.content,
            "default_content": self.content
        }
        self.assertEqual(default_dict, default_expected_result)

    def test_create_emojis(self):
        emojis = WebsiteContentCreation.create_emojis()
        emoji_1 = emojis[0]
        emoji_2 = emojis[1]
        self.assertTrue(emoji_1 in self.emojis)
        self.assertTrue(emoji_2 in self.emojis)

    def test_create_save_email(self):
        web_email_type = web_constants.CONTENT_FOR_ENGAGEMENT
        base_filters = {
            "for_content": social_constants.WEB,
            "purpose": web_email_type
        }

        title_filter = {}
        content_filter = {}
        title_filter.update(base_filters)
        content_filter.update(base_filters)

        title_dict = WebsiteContentCreation.create_title(None, title_filter)
        content_dict = WebsiteContentCreation.create_content(None, content_filter)
        first_emoji, last_emoji = WebsiteContentCreation.create_emojis()

        title = title_dict["title"]
        title_dict["title"] = f"{first_emoji}{title}{last_emoji}"
        type_related, created = WebsiteEmailsType.objects.get_or_create(slug=web_email_type)

        expected_web_email = WebsiteEmail.objects.create(
            type_related=type_related,
            **title_dict,
            **content_dict,
        )
        expected_web_email.title_emojis.add(first_emoji, last_emoji)

        web_email = WebsiteContentCreation.create_save_email(
            web_email_type
        )

        self.assertEqual(expected_web_email.title, web_email.title)
        self.assertEqual(expected_web_email.content, web_email.content)
        self.assertEqual(expected_web_email.default_title, web_email.default_title)
        self.assertEqual(expected_web_email.default_content, web_email.default_content)
        self.assertEqual(expected_web_email.title_emojis, web_email.title_emojis)
        self.assertEqual(expected_web_email.sent, web_email.sent)
        self.assertEqual(expected_web_email.date_to_send, web_email.date_to_send)