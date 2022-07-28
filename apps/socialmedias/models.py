from ckeditor.fields import RichTextField

from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    SET_NULL,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    JSONField,
    Model,
    PositiveIntegerField,
    TextField,
)

from apps.empresas.models import Company
from apps.escritos.models import Term
from apps.preguntas_respuestas.models import Question
from apps.public_blog.models import PublicBlog, WritterProfile
from apps.web import constants as web_constants

from .constants import FOR_CONTENT, POST_TYPE, SOCIAL_MEDIAS
from .managers import EmojisManager, HashtagsManager, TitlesManager, DefaultContentManager

User = get_user_model()


class Hashtag(Model):        
    title = TextField(default='')
    platform = CharField(max_length=500, choices=SOCIAL_MEDIAS)
    is_trending = BooleanField(default=False)
    objects = HashtagsManager()

    class Meta:
        verbose_name = "Default hashtags"
        db_table = 'socialmedia_hashtags'
    
    def __str__(self) -> str:
        return str(self.title)


class Emoji(Model):
    emoji = CharField(max_length=500)
    objects = EmojisManager()

    class Meta:
        verbose_name = "Default emojis"
        db_table = 'socialmedia_emojis'
    
    def __str__(self) -> str:
        return str(self.emoji)


class DefaultTilte(Model):
    title = TextField(default='')
    for_content = PositiveIntegerField(choices=FOR_CONTENT, blank=True, default=0)
    purpose = CharField(max_length=500, choices=web_constants.CONTENT_PURPOSES)
    objects = TitlesManager()

    class Meta:
        verbose_name = "Default titles"
        db_table = 'socialmedia_titles'
    
    def __str__(self) -> str:
        return str(self.title)


class DefaultContent(Model):
    title = CharField(max_length=500)
    for_content = PositiveIntegerField(choices=FOR_CONTENT, blank=True, default=0)
    purpose = CharField(max_length=500, choices=web_constants.CONTENT_PURPOSES)
    content = RichTextField()
    objects = DefaultContentManager()

    class Meta:
        verbose_name = "Default content"
        db_table = 'socialmedia_content'
    
    def __str__(self) -> str:
        return str(self.title)  


class BaseContentShared(Model):

    user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    date_shared = DateTimeField(auto_now_add=True)
    post_type = PositiveIntegerField(choices=POST_TYPE)
    platform_shared = CharField(max_length=500, choices=SOCIAL_MEDIAS)
    social_id = CharField(max_length=500)
    title = RichTextField(blank=True)
    description = RichTextField(blank=True)
    extra_description = RichTextField(blank=True)
    inside_information = RichTextField(blank=True)
    # original_post = JSONField(
    #     default={
    #         'url': '',
    #         'title': '',
    #         'local_id': '',
    #         'social_id': '',
    #         'post_type': '',
    #         'date_shared': ''
    #     }
    # )
    # 

    class Meta:
        abstract = True


class TermSharedHistorial(BaseContentShared):
    content_shared = ForeignKey(
        Term,
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name = 'terms_shared')

    class Meta:
        verbose_name = "Term shared"
        db_table = "shared_terms"


class QuestionSharedHistorial(BaseContentShared):
    content_shared = ForeignKey(
        Question,
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name = 'questions_shared')

    class Meta:
        verbose_name = "Question shared"
        db_table = "shared_questions"


class BlogSharedHistorial(BaseContentShared):
    content_shared = ForeignKey(
        PublicBlog,
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name = 'blogs_shared')

    class Meta:
        verbose_name = "Blog shared"
        db_table = "shared_blogs"


class ProfileSharedHistorial(BaseContentShared):
    content_shared = ForeignKey(
        WritterProfile,
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name = 'profiles_shared')
    
    class Meta:
        verbose_name = "Profile shared"
        db_table = "shared_profiles"


class CompanySharedHistorial(BaseContentShared):
    content_shared = ForeignKey(
        Company,
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name = 'company_shared')
    
    class Meta:
        verbose_name = "Company shared"
        db_table = "shared_companies"


class NewsSharedHistorial(BaseContentShared):
    company_related = ForeignKey(
        Company,
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name = 'news_shared')
    
    class Meta:
        verbose_name = "Company news shared"
        db_table = "shared_news"