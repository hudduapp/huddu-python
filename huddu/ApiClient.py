import json
import multiprocessing

import requests


class HudduClientException(Exception):
    pass


class ApiClient:
    def __init__(self, project: str, stream: str, token: str = None):
        """
        The main client for posting events to the huddu platform.
        :param project:
        :param stream:
        """
        self.project = project
        self.stream = stream

        self.headers = {"Content-Type": "application/json"}
        if token:
            self.headers["Authorization"] = f"Token {token}"

    def _request(self, body: dict) -> None:
        res = requests.request(
            "POST",
            f"https://ingest.huddu.io/{self.project}/{self.stream}",
            headers=self.headers,
            data=json.dumps(body),
        )

        if res.status_code > 299:
            print(res.json())

    def report(self, data: dict):
        p = multiprocessing.Process(
            target=self._request, args=[{"data": data}]
        )
        p.start()
