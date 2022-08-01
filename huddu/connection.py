import json

import requests


class Connection:
    def __init__(self, token: str) -> None:
        self.token = token
        self._base_url = "https://api.huddu.io"
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {token}"
        }

    def encode_body(self, body: dict) -> str:
        return json.dumps(
            body
        )

    def get(self, url: dict, params: dict) -> dict:
        res = requests.request("GET", url=f"{self._base_url}{url}", params=params, headers=self._headers)

        if res.status_code > 299:
            self.http_exception(
                f"The server returned an unexpected response\nstatus code: {res.status_code}\n\n{res.json()}")
        return res.json(), res.status_code

    def post(self, url: str, body: dict) -> dict:
        res = requests.request("POST", url=f"{self._base_url}{url}", body=self.encode_body(body),
                               headers=self._headers)

        if res.status_code > 299:
            self.http_exception(
                f"The server returned an unexpected response\nstatus code: {res.status_code}\n\n{res.json()}")
        return res.json(), res.status_code

    def put(self, url: str, body: dict) -> dict:
        res = requests.request("PUT", url=f"{self._base_url}{url}", body=self.encode_body(body),
                               headers=self._headers)

        if res.status_code > 299:
            self.http_exception(
                f"The server returned an unexpected response\nstatus code: {res.status_code}\n\n{res.json()}")
        return res.json(), res.status_code

    def patch(self, url: str, body: dict) -> dict:
        res = requests.request("PATCH", url=f"{self._base_url}{url}", body=self.encode_body(body),
                               headers=self._headers)

        if res.status_code > 299:
            self.http_exception(
                f"The server returned an unexpected response\nstatus code: {res.status_code}\n\n{res.json()}")
        return res.json(), res.status_code

    def delete(self, url: str, body: dict) -> dict:
        res = requests.request("DELETE", url=f"{self._base_url}{url}", body=self.encode_body(body),
                               headers=self._headers)

        if res.status_code > 299:
            self.http_exception(
                f"The server returned an unexpected response\nstatus code: {res.status_code}\n\n{res.json()}")
        return res.json(), res.status_code

    def http_exception(self, msg: str) -> None:
        raise Exception(msg)
