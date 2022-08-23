import os

from huddu.interceptors.Interceptor import Interceptor
from huddu.utils.APIClient import APIClient


class HudduClientException(Exception):
    pass


class HudduClient:
    def __init__(self, version: str, interceptor: Interceptor, project: str, token: str = None):
        """
        The main client for posting events to the huddu platform.

        Note that the token parameter will be overwritten by the HUDDU_TOKEN envvar if it is specified

        :param token:
        :param version:

        """

        self.APIClient = APIClient(
            token,
            project=project,
        )
        self.stream = None

        self.version = version
        self.token = os.getenv("HUDDU_TOKEN", token)
        if not self.token:
            raise HudduClientException(
                "A token has to be specified either via the token paramter or via the HUDDU_TOKEN envvar")

        print("Starting interceptor")
        self.interceptor = interceptor(self).start()

    def append(self, event: str, data: dict, meta=None):
        """
        handles stream creating, event creation
        :return:
        """

        if meta is None:
            meta = {}

        if not self.stream:
            self.stream = self.APIClient.create_or_return_stream(
                "django_log_v1")  # for now the streams name is the versions name
