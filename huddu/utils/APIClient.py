import json
from typing import List

import requests


class APIClient:
    def __init__(self, token: str, project: str, base_url: str = "https://api.huddu.io"):
        self.base_url = base_url
        self.project = project
        self.token = token
        self.headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json"
        }

    def create_or_return_stream(self, name: str, meta=None):
        """
        Create a new stream
        :param stream:
        :param name:
        :param meta:
        :return:
        """
        if meta is None:
            meta = {}
        res = requests.request("GET", f"{self.base_url}/projects/{self.project}/streams",
                               params={
                                   "query": f"name:{name}"
                               }, headers=self.headers)

        try:
            return res.json()["items"][0]
        except:
            res = requests.request("POST", f"{self.base_url}/projects/{self.project}/streams", headers=self.headers,
                                   data=json.dumps({
                                       "name": name,
                                       "meta": meta
                                   }))
            return res.json()["items"][0]

    def create_or_return_event(self, stream: str, components: List[str], name: str, description: str = None):
        """
        Create a new event
        :param components:
        :param name:
        :param description:
        :return:
        """

        requests.request("POST", f"{self.base_url}/projects/{self.project}/streams/{stream}/events",
                         headers=self.headers,
                         data=json.dumps({
                             "name": name,
                             "description": description,
                             "components": components,
                         }))

    def create_event_entry(self, stream: str, event: str, objects: List[dict]):
        """
        Create a new event entry (or multiple)
        :param stream:
        :param event:
        :param objects:
        :return:
        """

        requests.request("POST", f"{self.base_url}/projects/{self.project}/streams/{stream}/event/{event}/entries",
                         headers=self.headers,
                         data=json.dumps({
                             "objects": objects
                         }))
