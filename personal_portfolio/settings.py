"""
Django settings for personal_portfolio project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku
import dj_database_url
import dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "!^_6%0so9$a@u-w22nc56xcp0^spoo4k^3q!j016o5hll+#c#o"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'django_gulp',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bootstrap_modal_forms",
    # "sass_processor",
    "projects",
    # "resume",
    # "blog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
   
   'whitenoise.middleware.WhiteNoiseMiddleware',
   "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
]

ROOT_URLCONF = "personal_portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["personal_portfolio/templates/"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "personal_portfolio.wsgi.application"



# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    # DATABASES = {
        # "default": {
            # "ENGINE": "django.db.backends.postgresql_psycopg2",
            # "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        # }
    # }

    # DATABASES = {}
    DATABASES['default'] = dj_database_url.parse('postgres://pleevhxrkmgnpt:37eaa61b1148fbe771c47272aeebb258a44f4ff8da6abe7bf0ea7cfab04870b2@ec2-23-21-13-88.compute-1.amazonaws.com:5432/d9j311hdotp6lu')




# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        + ".UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        + ".MinimumLengthValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        + ".CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        + ".NumericPasswordValidator"
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Media information
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "projects/media")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'sass_processor.finders.CssFinder',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())

# del DATABASES['default']['OPTIONS']['sslmode']
# Django Sass
# SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR,'projects/static')

# COMPRESS_ROOT = '/compressed/'