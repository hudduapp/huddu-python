import os
import sys

from django.conf import settings

# use settings compatible with the installed Django version
# v1.10+ requires MIDDLEWARE keyname
# older versions require MIDDLEWARE_CLASSES keyname

ROLLBAR_CONFIG = {
    'access_token': 'POST_SERVER_ITEM_ACCESS_TOKEN',
    'environment': 'development',
    'branch': 'master',
    'root': os.getcwd()
}

MIDDLEWARE_CONFIG = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Rollbar middleware
    # 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
)

settings.configure(
    DEBUG=True,
    SECRET_KEY='bigsecret',
    ROOT_URLCONF=__name__,
    ROLLBAR=ROLLBAR_CONFIG,
    MIDDLEWARE=MIDDLEWARE_CONFIG,
)

HUDDU_CONFIG = {
    "project": "<project_id_or_name>",
    "stream": "<stream_id_or_name>",
    "environment": "development" if bool(int(settings.DEBUG)) else "production"
}

from django.urls import path
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')


def error(request):
    # method contains invalid syntax for instance:

    a == b

    return HttpResponse('Woops')


urlpatterns = (
    path('', index),
    path('errors', error),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
