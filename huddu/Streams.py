import time

from huddu.utils import _request


class Streams:
    def __init__(self, api_key):
        self.api_key = api_key

    def list(self, project: str, account: str, skip: int = 0, limit: int = 25):
        return _request(
            self.api_key,
            "GET",
            f"/accounts/{account}/projects/{project}/streams",
            params={"skip": skip, "limit": limit},
        )

    def get(
        self,
        id: str,
        project: str,
        account: str,
    ):
        return _request(
            self.api_key, "GET", f"/accounts/{account}/projects/{project}/streams/{id}"
        )

    def list_versions(
        self,
        id: str,
        project: str,
        account: str,
    ):
        return _request(
            self.api_key,
            "GET",
            f"/accounts/{account}/projects/{project}/streams/{id}/versions",
        )

    def create(self, project: str, account: str, name: str):
        return _request(
            self.api_key,
            "POST",
            f"/accounts/{account}/projects/{project}/streams",
            data={"name": name},
        )

    def create_version(
        self, id: str, project: str, account: str, version: str = None, name: str = None
    ):
        payload = {}
        if name:
            payload["name"] = name
        if version:
            payload["version"] = version
        else:
            payload["version"] = int(time.time())

        return _request(
            self.api_key,
            "POST",
            f"/accounts/{account}/projects/{project}/streams/{id}/versions",
            data=payload,
        )
