from typing import List, Any

from huddu.utils import _request


class Events:
    def __init__(self, api_key):
        self.api_key = api_key

    def list(
        self, account: str, project: str, stream: str, skip: int = 0, limit: int = 25
    ):
        return _request(
            self.api_key,
            "GET",
            f"/accounts/{account}/projects/{project}/streams/{stream}/events",
            params={"skip": skip, "limit": limit},
        )

    def search(
        self,
        account: str,
        project: str,
        stream: str,
        query: dict,
        skip: int = 0,
        limit: int = 25,
    ):
        payload = {"limit": limit, "skip": skip, "query": query}

        return _request(
            self.api_key,
            "POST",
            f"/accounts/{account}/projects/{project}/streams/{stream}/events/search",
            data=payload,
        )

    def get(self, id: str, account: str, project: str, stream: str):
        return _request(
            self.api_key,
            "GET",
            f"/accounts/{account}/projects/{project}/streams/{stream}/events/{id}",
        )

    def create(
        self,
        account: str,
        project: str,
        stream: str,
        batch: List[Any] = None,
        data: Any = None,
    ):

        payload = {}
        if data:
            payload["data"] = data

        if batch:
            payload["batch"] = batch

        if not batch and not data:
            raise Exception("One of data or batch is required.")

        return _request(
            self.api_key,
            "POST",
            f"/accounts/{account}/projects/{project}/streams/{stream}/events",
            data=payload,
        )

    def update(self, account: str, project: str, stream: str, event: str, meta: dict):

        payload = {}
        if meta:
            payload["meta"] = meta

        return _request(
            self.api_key,
            "PUT",
            f"/accounts/{account}/projects/{project}/streams/{stream}/events/{event}",
            data=payload,
        )
