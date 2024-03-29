from celery import shared_task

from src.content_creation import constants
from src.socialmedias.constants import FACEBOOK, TWITTER

from .outils.poster import SocialPosting


@shared_task(autoretry_for=(Exception,), max_retries=3)
def socialmedia_share_company():
    SocialPosting.share_content(
        constants.COMPANY_FOR_CONTENT,
        [
            {"platform_shared": FACEBOOK, "post_type": constants.POST_TYPE_TEXT_IMAGE},
            {"platform_shared": TWITTER, "post_type": constants.POST_TYPE_TEXT_IMAGE},
        ],
    )


@shared_task(autoretry_for=(Exception,), max_retries=3)
def socialmedia_share_news():
    SocialPosting.share_content(
        constants.NEWS_FOR_CONTENT,
        [
            {"platform_shared": FACEBOOK, "post_type": constants.POST_TYPE_TEXT_IMAGE},
            {"platform_shared": TWITTER, "post_type": constants.POST_TYPE_TEXT_IMAGE},
        ],
    )


@shared_task(autoretry_for=(Exception,), max_retries=3)
def socialmedia_share_term():
    SocialPosting.share_content(
        constants.TERM_FOR_CONTENT,
        [
            {"platform_shared": FACEBOOK, "post_type": constants.POST_TYPE_TEXT_IMAGE},
            {"platform_shared": TWITTER, "post_type": constants.POST_TYPE_TEXT_IMAGE},
        ],
    )


@shared_task(autoretry_for=(Exception,), max_retries=3)
def socialmedia_share_blog():
    SocialPosting.share_content(
        constants.PUBLIC_BLOG_FOR_CONTENT,
        [
            # {"platform_shared": FACEBOOK, "post_type": constants.POST_TYPE_TEXT_IMAGE},
            {"platform_shared": TWITTER, "post_type": constants.POST_TYPE_TEXT_IMAGE},
        ],
    )


@shared_task(autoretry_for=(Exception,), max_retries=3)
def socialmedia_share_question():
    SocialPosting.share_content(
        constants.QUESTION_FOR_CONTENT,
        [
            # {"platform_shared": FACEBOOK, "post_type": constants.POST_TYPE_TEXT_IMAGE},
            {"platform_shared": TWITTER, "post_type": constants.POST_TYPE_TEXT_IMAGE},
        ],
    )
