import random
from typing import Any, Dict

from django.conf import settings

from src.recsys.mixins import RecommenderMixin


class FastContextView:
    custom_context_data: Dict[str, Any] = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(**self.custom_context_data)
        return context


class SEOViewMixin(FastContextView, RecommenderMixin):
    """
    Mixin to populate meta information for SEO purpose

    meta_description
    meta_tags
    meta_title
    meta_url
    meta_image
    meta_author
    meta_category
    is_article
    open_graph_type
    update_visits

    open_graph_type might be = website, article, or video
    https://ogp.me/#types
    """

    meta_description: str = ""
    meta_tags: str = ""
    meta_title: str = ""
    meta_url: str = ""
    meta_image: str = ""
    meta_author: str = ""
    meta_category: str = ""
    is_article: bool = False
    open_graph_type: str = "website"
    update_visits: bool = False
    no_index: bool = False
    no_follow: bool = False
    private_view: bool = False

    def update_views(self, instance):
        instance.total_views += 1
        instance.save(update_fields=["total_views"])

    def get_possible_meta_attribute(self, instance: object, fields: list, default: str):
        meta_field = default
        if instance:
            for field in fields:
                possible_meta_field = getattr(instance, field, None)
                if possible_meta_field is not None:
                    meta_field = possible_meta_field
                    break
        return meta_field

    def get_meta_url(self):
        meta_url = self.meta_url
        if not meta_url:
            meta_url = self.request.path
        return meta_url

    def get_meta_author(self, instance: object = None):
        meta_author = self.meta_author
        if not meta_author:
            meta_author = self.get_possible_meta_attribute(instance, ["meta_author", "author"], "InvFin")
        return meta_author

    def get_meta_title(self, instance: object = None):
        meta_title = self.meta_title
        if not meta_title:
            if self.private_view:
                meta_title = self.__class__.__name__
            else:
                meta_title = self.get_possible_meta_attribute(
                    instance, ["meta_title", "name", "title"], "Invierte correctamente"
                )
        return meta_title

    def get_meta_description(self, instance: object = None):
        meta_description = self.meta_description
        if not meta_description:
            meta_description = self.get_possible_meta_attribute(
                instance,
                ["meta_description", "resume", "description", "content"],
                "Todo lo que necesitas para ser un mejor inversor",
            )
        return meta_description

    def get_meta_image(self, instance: object = None):
        meta_image = self.meta_image
        if not meta_image:
            if instance:
                meta_image = self.get_possible_meta_attribute(
                    instance, ["meta_image", "regularised_image", "image", "thumbnail"], ""
                )
                if not meta_image:
                    author = getattr(instance, "author", None)
                    if author:
                        meta_image = author.foto
            else:
                selected_image = random.choice(
                    [
                        "favicon/favicon.ico",
                        "general/exchange.webp",
                        "general/hero-img.webp",
                        "general/why-us.webp",
                    ]
                )
                meta_image = f"/static/general/assets/img/{selected_image}"

        if not meta_image.startswith("http"):
            meta_image = f"{settings.FULL_DOMAIN}{meta_image}"

        return meta_image

    def get_meta_tags(self) -> str:
        meta_tags = self.meta_tags
        if not meta_tags:
            meta_tags = "finanzas, blog financiero, blog el financiera, invertir"
        return meta_tags

    def get_meta_category(self, instance: object = None):
        meta_category = self.meta_category
        if not meta_category:
            meta_category = self.get_possible_meta_attribute(instance, ["category"], "Inversiones")
        return meta_category

    def get_meta_twitter_author(self):
        return "@InvFinz"

    def get_open_graph_type(self):
        return self.open_graph_type

    def get_meta_published_time(self, instance: object = None):
        return self.get_possible_meta_attribute(instance, ["published_at"], None)

    def get_meta_modified_time(self, instance: object = None):
        return self.get_possible_meta_attribute(instance, ["updated_at"], None)

    def get_schema_org(self, instance: object = None) -> Dict:
        return getattr(instance, "schema_org", {})

    def get_meta_robots(self):
        if self.private_view:
            return "nofollow,noindex"
        if not self.no_follow and not self.no_index:
            return None
        elif self.no_follow and not self.no_index:
            return "nofollow"
        elif not self.no_follow and self.no_index:
            return "noindex"
        else:
            return "nofollow,noindex"

    def get_base_meta_information(self, instance: object = None):
        return {
            "meta_robots": self.get_meta_robots(),
            "meta_description": self.get_meta_description(instance),
            "meta_tags": self.get_meta_tags(),
            "meta_title": self.get_meta_title(instance),
            "meta_url": self.get_meta_url(),
            "meta_author": self.get_meta_author(instance),
            "meta_image": self.get_meta_image(instance),
            "is_article": self.is_article,
            "meta_category": self.get_meta_category(instance),
            "meta_twitter_author": self.get_meta_twitter_author(),
            "open_graph_type": self.get_open_graph_type(),
            "schema_org": self.get_schema_org(instance),
        }

    def get_meta_information(self, instance: object = None):
        base_meta_information = self.get_base_meta_information(instance)
        if self.is_article:
            base_meta_information.update(
                {
                    "meta_published_time": self.get_meta_published_time(instance),
                    "meta_modified_time": self.get_meta_modified_time(instance),
                }
            )
        return base_meta_information

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            instance = self.object
        except Exception:
            instance = None
        context.update(self.get_meta_information(instance))
        if self.update_visits:
            self.update_views(instance)
        return context
