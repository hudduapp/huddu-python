import json
from typing import List

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

        self.headers = {
            "Content-Type": "application/json"
        }

    def report(self, event_type: str, objects: List[dict]):
        print(objects)
        res = requests.request("POST", f"https://ingest.huddu.io/{self.project}/{self.stream}/{event_type}",
                               headers=self.headers, data=json.dumps(
                {
                    
                    "objects": objects
                }
            ))
        print(res.json())
