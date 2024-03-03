import os
from pathlib import Path

from .helper.jazzmin import *

from .helper.env_reader import env

BASE_DIR = Path(__file__).resolve().parent.parent

PRODUCTION = env("PRODUCTION", default=False, cast=bool)

SECRET_KEY = env("SECRET_KEY")


THEME_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "drf_yasg",
    "ratelimit",
    "corsheaders",
    "django_summernote",
    'debug_toolbar',
]

APPS = [
    "blog_and_news",
    "client_actions",
    "tour",
    "main_page",
    "transport",
]

THEME = [
    'jazzmin',
]

INSTALLED_APPS = [
    *THEME,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THEME_PARTY_APPS,
    *APPS
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

CORS_ALLOW_ALL_ORIGINS = True


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

DEFAULT_CHARSET = 'utf-8'

FILE_CHARSET = 'utf-8'

DEFAULT_CONTENT_TYPE = 'text/html; charset=utf-8'

USE_I18N = True

USE_TZ = True

SUMMERNOTE_CONFIG = {
    'summernote': {
        'callbacks': {
            'onImageUpload': 'core.summernote_custom.upload_image'
        }
    }
}

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.joinpath("static/")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.joinpath("media/")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if not PRODUCTION:
    from .local import *
else:
    from .prod import *

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

