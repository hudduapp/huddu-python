from abc import ABC

try:
    import time

except:
    raise NotImplemented("huddu | django is not installed")

from huddu.interceptors.Interceptor import Interceptor


class DjangoMiddleware(Interceptor, ABC):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        What does Huddu log:

        - Reason Pharase (to be displayed in a terminal
        -

        """

        response = self.get_response(request)
        print(dir(response))

        return response

    def start(self):
        self.client.report(
            "dummy_event",
            [{
                "a": "b"
            }]
        )
