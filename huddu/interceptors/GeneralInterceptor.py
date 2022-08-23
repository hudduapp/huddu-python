from huddu.interceptors.Interceptor import Interceptor


class GeneralInterceptor(Interceptor):

    def start(self):
        self.client.append(
            "dummy_event",
            [{
                "a": "b"
            }]
        )
