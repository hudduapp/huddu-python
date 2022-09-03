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
        self.client.make_suggestions("django_logs", [
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

        self._log_event(
            response.reason_phrase,
            request.path,
            int(response.status_code),
            request.method,
        )

        return response

    def _log_event(self, line, path, status_code, method):
        color = "white"

        if str(status_code)[:1] == "5":
            color = "red"
        if str(status_code)[:1] == "4":
            color = "yellow"
        if str(status_code)[:1] == "3":
            color = "purple"
        if str(status_code)[:1] == "1":
            color = "blue"
        objects = [
            {
                "data": {
                    "line": f"{method.upper()} {path} {status_code} | {line}",
                    "color": color,
                }
            }
        ]

        self.client.report("django_logs", objects)
