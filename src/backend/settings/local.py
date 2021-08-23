# flake8: noqa
import os

from settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# CORS_ORIGIN_ALLOW_ALL = True
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': os.environ['MAIN_DB_NAME'],
    #     'USER': 'postgres',
    #     'PASSWORD': os.environ['POSTGRES_PASSWORD'],
    #     'HOST': 'db',
    #     'PORT': '5432',
    # }
}
