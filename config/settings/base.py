from pathlib import Path

import environ
from django.contrib.messages import constants as messages
from imagekitio import ImageKit

from .ckeditor import *

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# invfin/
APPS_DIR = ROOT_DIR / "apps"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
CURRENT_DOMAIN = env("CURRENT_DOMAIN")
MAIN_DOMAIN = env("MAIN_DOMAIN")
FULL_DOMAIN = env("FULL_DOMAIN")

PROD_ENV = CURRENT_DOMAIN != MAIN_DOMAIN

PROTOCOL = "https://" if PROD_ENV else "http://"

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", True)

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "CET"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "es-ES"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = False
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = False
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

DATE_INPUT_FORMATS = [
    '%d/%m/%Y',  # '10/25/06'
    '%d-%m-%Y',  # '10-25-06'
]

DATETIME_INPUT_FORMATS = [
    '%d/%m/%Y %H:%M:%S',     # '10/25/06'
    '%d-%m-%Y %H:%M',        # '10-25-06'
    '%d/%m/%Y %H:%M:%S',     # '10/25/06'
    '%d-%m-%Y %H:%M',        # '10-25-06'
]

# Boolean that sets whether to add thousand separator when formatting numbers
USE_THOUSAND_SEPARATOR = True

# Number of digits that will be together, when splitting them by
# THOUSAND_SEPARATOR. 0 means no grouping, 3 means splitting by thousands...
NUMBER_GROUPING = 3

# Thousand separator symbol
THOUSAND_SEPARATOR = "."

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.admin",
    "django.forms",
    "django.contrib.sitemaps",
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    "crispy_forms",
    "crispy_bootstrap5",
    "django_celery_beat",
    "rest_framework",
    "corsheaders",
    "ckeditor",
    "django_cleanup.apps.CleanupConfig",
    "django_countries",
    "import_export",
    "admin_honeypot",
    'widget_tweaks',
    'django_json_widget',
]

LOCAL_APPS = [
    "apps.users",
    "apps.general",
    "apps.seo",
    "apps.escritos",
    "apps.web",
    "apps.preguntas_respuestas",
    "apps.public_blog",
    "apps.empresas",
    "apps.super_investors",
    "apps.etfs",
    "apps.screener",
    "apps.cartera",
    "apps.roboadvisor",
    "apps.socialmedias",
    "apps.api",
    "apps.business",
    "apps.recsys",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "apps.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    'allauth.account.auth_backends.AuthenticationBackend',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:user_inicio"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "general.middleware.SubdomainURLRoutingMiddleware",
    "seo.middleware.VisiteurMiddleware",
]

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_NAME = "sessionid"
SESSION_COOKIE_DOMAIN = f".{CURRENT_DOMAIN}"
# Whether to save the session data on every request.
SESSION_SAVE_EVERY_REQUEST = False
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_DOMAIN = f".{CURRENT_DOMAIN}"
CSRF_TRUSTED_ORIGINS = [f".{CURRENT_DOMAIN}", f"{CURRENT_DOMAIN}"]
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(APPS_DIR / "static")
    ]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [Path(f"{APPS_DIR}/templates/")],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,

        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "apps.users.context_processors.allauth_settings",
                "apps.users.context_processors.users_notifications",
                "apps.users.context_processors.user_companies_visited",
                "apps.public_blog.context_processors.keep_email",
                "apps.seo.context_processors.journey",
                "apps.seo.context_processors.debug",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

EMAIL_CONTACT = env("EMAIL_CONTACT")
EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX")
DEFAULT_EMAIL = env("DEFAULT_EMAIL")
EMAIL_NEWSLETTER = env("EMAIL_NEWSLETTER")
MAIN_EMAIL = env("MAIN_EMAIL")
EMAIL_ACCOUNTS = env("EMAIL_ACCOUNTS")
EMAIL_DEFAULT = env("EMAIL_DEFAULT")
EMAIL_SUGGESTIONS = env("EMAIL_SUGGESTIONS")

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
SECOND_ADMIN_URL = "admin2/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Lucas montes""", "lluc23@hotmail.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}


# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_SESSION_REMEMBER = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "apps.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
ACCOUNT_FORMS = {"signup": "apps.users.forms.UserSignupForm"}
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "apps.users.adapters.SocialAccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
SOCIALACCOUNT_FORMS = {"signup": "apps.users.forms.UserSocialSignupForm"}

# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 5 * 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

if DEBUG:
    CELERY_TASK_EAGER_PROPAGATES = True

# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
DRF_DEFAULT_RENDERER_CLASSES = {"DRF_DEFAULT_RENDERER_CLASSES": 'rest_framework.renderers.JSONRenderer'}
DEFAULT_SCHEMA_CLASS = {}
if DEBUG:
    DRF_DEFAULT_RENDERER_CLASSES = {"DRF_DEFAULT_RENDERER_CLASSES": 'rest_framework.renderers.BrowsableAPIRenderer'}
    DEFAULT_SCHEMA_CLASS = {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}

REST_FRAMEWORK = {
    **DEFAULT_SCHEMA_CLASS,
    **DRF_DEFAULT_RENDERER_CLASSES,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework.authentication.SessionAuthentication',
        "apps.api.authentication.KeyAuthentication",
        'rest_framework.authentication.BasicAuthentication',
    ],
    "DEFAULT_PERMISSION_CLASSES": ["apps.api.permissions.ReadOnly"],
    'DEFAULT_VERSIONING_CLASS': "rest_framework.versioning.NamespaceVersioning",
    'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'example.throttles.BurstRateThrottle',
    #     'example.throttles.SustainedRateThrottle'
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'burst': '60/min',
    #     'sustained': '1000/day'
    # }
}

# By Default swagger ui is available only to admin user. You can change permission classs to change that
# See more configuration options at https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings
SPECTACULAR_SETTINGS = {
    "TITLE": "InvFin API",
    "DESCRIPTION": "Documentation of API endpoints of InvFin",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SERVERS": [
        {"url": f"http://0.0.0.0:8000", "description": "Local Development server"},
        {"url": f"http://127.0.0.1:8000", "description": "Local Development server"},
        {"url": f"http://example.com:8000", "description": "Local Development server"},
        {"url": f"https://inversionesyfinanzas.xyz", "description": "Production server"},
    ],
}
# API versions
# ------------------------------------------------------------------------------
API_VERSION = {'CURRENT_VERSION': 'v1'}



# Tags
# ------------------------------------------------------------------------------
# MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# GEOIP
# ------------------------------------------------------------------------------
GEOIP_PATH = str(ROOT_DIR / "geoip")

# Financial data KEYS
# ------------------------------------------------------------------------------
FINNHUB_TOKEN = env.str("FINNHUB_TOKEN")
FINNHUB_SANDBOX_TOKEN = env.str("FINNHUB_SANDBOX_TOKEN")
FINPREP_KEY = env.str("FINPREP_KEY")

# GOOGLE KEYS
# ------------------------------------------------------------------------------
GOOGLE_RECAPTCHA_SECRET_KEY = env.str('GOOGLE_RECAPTCHA_SECRET_KEY')
GOOGLE_RECAPTCHA_PUBLIC_KEY = env.str('GOOGLE_RECAPTCHA_PUBLIC_KEY')

# FACEBOOK KEYS
# ------------------------------------------------------------------------------
OLD_FB_PAGE_ACCESS_TOKEN = env.str('OLD_FB_PAGE_ACCESS_TOKEN')
NEW_FB_PAGE_ACCESS_TOKEN = env.str('NEW_FB_PAGE_ACCESS_TOKEN')
FACEBOOK_APP_SECRET = env.str('FACEBOOK_APP_SECRET')
OLD_FACEBOOK_ID = env.str('OLD_FACEBOOK_ID')
NEW_FACEBOOK_ID = env.str('NEW_FACEBOOK_ID')
FB_USER_ACCESS_TOKEN = env.str('FB_USER_ACCESS_TOKEN')

# INSTAGRAM KEYS
# ------------------------------------------------------------------------------
INSTAGRAM_ID = env.str('INSTAGRAM_ID')

# TWITTER KEYS
# ------------------------------------------------------------------------------
TWITTER_CONSUMER_KEY = env.str('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = env.str('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = env.str('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = env.str('TWITTER_ACCESS_TOKEN_SECRET')


# List of compiled regular expression objects representing User-Agent strings
# that are not allowed to visit any page, systemwide. Use this for bad
# robots/crawlers. Here are a few examples:
#     import re
#     DISALLOWED_USER_AGENTS = [
#         re.compile(r'^NaverBot.*'),
#         re.compile(r'^EmailSiphon.*'),
#         re.compile(r'^SiteSucker.*'),
#         re.compile(r'^sohu-search'),
#     ]

# IMAKIT
# ------------------------------------------------------------------------------
IMAGEKIT_PRIVATE_KEY = env.str('IMAGEKIT_PRIVATE_KEY')
IMAGEKIT_PUBLIC_KEY = env.str('IMAGEKIT_PUBLIC_KEY')
IMAGEKIT_URL_ENDPOINT = env.str('IMAGEKIT_URL_ENDPOINT')

IMAGE_KIT = ImageKit(
    private_key=IMAGEKIT_PRIVATE_KEY,
    public_key=IMAGEKIT_PUBLIC_KEY,
    url_endpoint=IMAGEKIT_URL_ENDPOINT
)

# STRIPE
# ------------------------------------------------------------------------------
STRIPE_PRIVATE = env.str('STRIPE_PRIVATE')
STRIPE_PUBLIC = env.str('STRIPE_PUBLIC')
WEBHOOK_SECRET = env.str('WEBHOOK_SECRET')
