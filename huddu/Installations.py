from huddu.utils import _request


class Installations:
    def __init__(self, api_key):
        self.api_key = api_key

    def list(self, skip: int = 0, limit: int = 25, code: str = None):
        params = {"skip": skip, "limit": limit}

        if code:
            params["code"] = code

        return _request(
            self.api_key, "GET", "/installations", params=params
        )

    def get(self, id: str):
        return _request(self.api_key, "GET", f"/installations/{id}")

    def update(self, id: str, meta: list = None):
        payload = {}
        if meta:
            payload["meta"] = meta

        return _request(self.api_key, "PUT", f"/installations/{id}", data=payload)
