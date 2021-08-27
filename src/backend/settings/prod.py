# flake8: noqa
from aws.utils import get_db_connection_params, get_secret
from settings.base import *

secret_variables = get_secret(
    os.environ['AWS_SECRET_NAME'],
    os.environ['AWS_REGION_NAME'],
)
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = secret_variables['DJANGO_SECRET_KEY']

DEBUG = False

# TODO temp cors disable
ALLOWED_HOSTS = ['*']
# CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {'default': get_db_connection_params(secret_variables)}

REST_FRAMEWORK.update(
    {'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',)}
)

