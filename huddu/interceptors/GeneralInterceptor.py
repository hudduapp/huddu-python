from huddu.interceptors.Interceptor import Interceptor


class GeneralInterceptor(Interceptor):

    def start(self):
        self.client.report(
            "dummy_event",
            [{
                "a": "b"
            }]
        )
