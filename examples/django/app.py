import sys
from django.conf import settings


# This is the HUDDU_CONFIG which will be read by the middleware
# Note that this has to be set under the **HUDDU** variable in your settings!
HUDDU_CONFIG = {
    "project": "6972870869211324416",  # the project identifier
    "stream": "a-stream",  # the streams name/identifier (if you use stream ids you will always write to that stream; with names events will be written to the newest version)
    "environment": "debug",  # the environment | optional (the default value is debug)
}


MIDDLEWARE_CONFIG = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Here we register the huddu DjangoMiddleware!
    "huddu.interceptors.django.middleware.DjangoMiddleware",
)

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=["*"],
    SECRET_KEY="bigsecret",
    ROOT_URLCONF=__name__,
    HUDDU=HUDDU_CONFIG,
    MIDDLEWARE=MIDDLEWARE_CONFIG,
)

from django.urls import path
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")


def error(request):
    # an example error in your code
    a == b
    return HttpResponse("Woops")


urlpatterns = (
    path("", index),
    path("errors", error),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
