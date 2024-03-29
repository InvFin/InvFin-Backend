"""
With these settings, tests run faster.
"""
from .base import *  # noqa
from .base import ROOT_DIR, env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="jBxqwRsGQcTz3dV1o8quZxpFMyKBGhF2Olha3VTA7TTALWfgFkrLuY0dQYLoOnp7",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("LOCAL_DATABASE_URL", default="postgresql://root@localhost/circle_test?sslmode=disable")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Your stuff...
# ------------------------------------------------------------------------------
GEOIP_PATH = str(ROOT_DIR / "test-geoip")
GEOIP_CITY = "GeoIP2-City.mmdb"

EMAIL_CONTACT = "EMAIL_CONTACT@example.com"
EMAIL_SUBJECT_PREFIX = "EMAIL_SUBJECT_PREFIX@example.com"
DEFAULT_EMAIL = "DEFAULT_EMAIL@example.com"
EMAIL_NEWSLETTER = "EMAIL_NEWSLETTER@example.com"
MAIN_EMAIL = "MAIN_EMAIL@example.com"
EMAIL_ACCOUNTS = "EMAIL_ACCOUNTS@example.com"
EMAIL_DEFAULT = "EMAIL_DEFAULT@example.com"
EMAIL_SUGGESTIONS = "EMAIL_SUGGESTIONS@example.com"
