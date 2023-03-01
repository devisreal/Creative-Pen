"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, seeclear
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import cloudinary
import cloudinary.api
import cloudinary.uploader
import os
import dj_database_url
from pathlib import Path
from decouple import config, Csv
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
MODE = config("MODE", default="dev")
# SECRET_KEY = config("SECRET_KEY")
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
DEBUG = 'RENDER' not in os.environ

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "crispy_forms",
    "crispy_bootstrap5",
    "taggit",
    "taggit_selectize",
    "active_link",
    "hitcount",
    "froala_editor",
    'django_cleanup.apps.CleanupConfig',
    'cloudinary_storage',
    "cloudinary",
    # Custom Apps
    "account",
    "blog",
    "pen_admin",
    "users",
    "pages",
]


cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME"),
    api_key=config("CLOUDINARY_API_KEY"),
    api_secret=config("CLOUDINARY_API_SECRET")
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': config("CLOUDINARY_API_KEY"),
    'API_SECRET': config("CLOUDINARY_API_SECRET")
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "pages.context_processors.categories_processor",
                # 'django.core.context_processors',
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if config("MODE") == "dev":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "PORT": "",
        }
    }
# production
else:
    DATABASES = {"default": dj_database_url.config(
        default=config("DATABASE_URL"))}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "creative_pen/"
MEDIA_ROOT = BASE_DIR / "media"
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Froala Editor
FRAOLA_EDITOR_THIRD_PARTY = ("image_aviary", "spell_checker")
FROALA_STORAGE_BACKEND = 'cloudinary_storage.storage.MediaCloudinaryStorage'
FROALA_UPLOAD_PARAMS = {
    'folder': 'media',
    'tags': 'froala_editor'
}
FROALA_UPLOAD_URL = 'http://res.cloudinary.com/ds4h5p2np/image/upload/q_auto/'
FROALA_UPLOAD_PATH = 'froala_editor_upload/'
FROALA_EDITOR_OPTIONS = {
    'imageUploadURL': '/froala_upload/',
    'imageAllowedTypes': ['jpeg', 'jpg', 'png', 'gif'],
}

MESSAGE_TAGS = {
    messages.ERROR: "danger",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.INFO: "info",
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap4"
AUTH_USER_MODEL = "account.User"
LOGIN_URL = "login"

# DJANGO SESSION TIMEOUT SETTINGS
# SESSION_EXPIRE_SECONDS = 7200
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY = False
# SESSION_TIMEOUT_REDIRECT = 'login'

# DJANGO TAGGIT CONFIG
TAGGIT_CASE_INSENSITIVE = True
TAGGIT_TAGS_FROM_STRING = "taggit_selectize.utils.parse_tags"
TAGGIT_STRING_FROM_TAGS = "taggit_selectize.utils.join_tags"
TAGGIT_SELECTIZE = {
    'MINIMUM_QUERY_LENGTH': 2,
    'RECOMMENDATION_LIMIT': 10,
    'CSS_FILENAMES': ("taggit_selectize/css/selectize.django.css",),
    'JS_FILENAMES': ("taggit_selectize/js/selectize.js",),
    'DIACRITICS': True,
    'CREATE': True,
    'PERSIST': True,
    'OPEN_ON_FOCUS': True,
    'HIDE_SELECTED': True,
    'CLOSE_AFTER_SELECT': False,
    'LOAD_THROTTLE': 300,
    'PRELOAD': False,
    'ADD_PRECEDENCE': True,
    'SELECT_ON_TAB': True,
    'REMOVE_BUTTON': True,
    'RESTORE_ON_BACKSPACE': True,
    'DRAG_DROP': False,
    'DELIMITER': ','
}
