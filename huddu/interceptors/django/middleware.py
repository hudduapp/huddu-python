import sys
import traceback
from abc import ABC

from huddu import ApiClient

try:
    from django.conf import settings
except:
    raise NotImplemented("huddu | django is not installed")

from huddu.interceptors.Interceptor import Interceptor


class DjangoMiddleware(Interceptor, ABC):
    def __init__(self, get_response):
        self.get_response = get_response
        self._make_client()

    def _make_client(self) -> ApiClient:
        config = settings.HUDDU
        self.client = ApiClient(project=config["project"], stream=config["stream"])
        self.client.make_suggestions("error_logs", [
            "6967511878721511424"])  # huddu/console  (https://huddu.io/marketplace/6967511878721511424)

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

        self.client.report("response_metrics", [{
            "data": {
                response["status_code"]: 1
            }
        }])
        return response

    def process_exception(self, request, exception):
        _, _, stacktrace = sys.exc_info()
        #        print(''.join(traceback.format_tb(stacktrace)))
        self.client.report("error_logs", [{
            "data": {
                "line": f"{request.method} {request.path}\n---\nException:\n{exception}\n\nStacktrace:\n{''.join(traceback.format_tb(stacktrace))}",
                "color": "red"
            }
        }])
