from django.apps import AppConfig


class BusinessConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.business"

    def ready(self):
        import src.business.signals.signals  # noqa