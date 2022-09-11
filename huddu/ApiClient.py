import json

import requests


class HudduClientException(Exception):
    pass


class ApiClient:
    def __init__(self, project: str, stream: str):
        """
        The main client for posting events to the huddu platform.

        Note that the token parameter will be overwritten by the HUDDU_TOKEN envvar if it is specified
        :param project:
        :param stream:
        """
        self.project = project
        self.stream = stream

        self.headers = {"Content-Type": "application/json"}

    def report(self, event_type: str, data: dict):
        requests.request(
            "POST",
            f"https://ingest.huddu.io/{self.project}/{self.stream}/{event_type}",
            headers=self.headers,
            data=json.dumps({"data": data}),
        )

    def suggest_components(self, event_type: str, components: list):
        self.report(event_type, {
            "components": components,
            "skip": True
        })
        print("-- making suggestions")
