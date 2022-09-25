import sys
import traceback
from abc import ABC

import pkg_resources

from huddu import ApiClient

try:
    from django.conf import settings
except:
    raise NotImplemented("huddu >> django is not installed")

from huddu.interceptors.Interceptor import Interceptor


class DjangoMiddleware(Interceptor, ABC):
    def __init__(self, get_response):
        self.get_response = get_response
        self.config = settings.HUDDU
        self._make_client()

    def _make_client(self) -> ApiClient:
        config = settings.HUDDU
        self.client = ApiClient(project=config["project"], stream=config["stream"], token=config.get("token", None))

    def __call__(self, request):
        """
        What does Huddu log:

        - response.reason_phrase
        - response.status_code
        - request.content_type
        - request.path
        - request.scheme => protocol
        - request.body
        - request.headers
        - request.method
        """

        response = self.get_response(request)

        self.client.report(
            "response_metrics",
            {
                "field": response.status_code,
                "value": 1,
            },
            meta={
                "env": self.config.get("environment", self.config.get("env", "debug")),
            }
        )
        return response

    def process_exception(self, request, exception):
        _exception, _error, stacktrace = sys.exc_info()
        installed_packages = pkg_resources.working_set
        installed_packages_list = sorted(
            ["%s==%s" % (i.key, i.version) for i in installed_packages]
        )
        packages = ""
        for i in installed_packages_list:
            packages += f"- {i}\n"

        markdown = (
            "# ❌ Error\n"
            f"\t{str(_error)}\n"
            "### Exception\n"
            f"\t{str(_exception)}\n"
            "### Stacktrace\n"
            "<pre><code>"
        )

        # weird stuff happens with the stacktrace
        markdown += (
                "".join(traceback.format_tb(stacktrace)) + "\n"
                                                           "</pre></code>\n"
                                                           "# ⚙️ Environment\n"
        )

        markdown += (
                "<mark>"
                + self.config.get("environment", self.config.get("env", "debug"))
                + "</mark>\n"
        )
        markdown += "### Packages\n" f"{packages}\n" "### Version\n" f"{sys.version})"

        self.client.report("error_logs", {"markdown": markdown},
                           meta={
                               "env": self.config.get("environment", self.config.get("env", "debug")),
                           })
