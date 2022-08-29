from huddu.interceptors.Interceptor import Interceptor


class DjangoMiddleware(Interceptor):

    def start(self):
        self.client.report(
            "dummy_event",
            [{
                "a": "b"
            }]
        )
