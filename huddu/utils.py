import json
from urllib import parse

from requests import Session


class CustomSession(Session):
    def rebuild_auth(self, prepared_request, response):
        """
        No code here means requests will always preserve the Authorization
        header when redirected.
        Be careful not to leak your credentials to untrusted hosts!
        """


def _request(api_key, method, url, params=None, data=None):
    headers = {"Authorization": f"Token {api_key}"}

    base_url = "https://api.huddu.io"

    if params:
        url += "?" + parse.urlencode(params)

    s = CustomSession()

    if data:
        payload = json.dumps(data)
        res = s.request(method, f"{base_url}{url}", data=payload, headers=headers)
    else:
        res = s.request(method, f"{base_url}{url}", headers=headers)

    if res.status_code > 299:
        raise Exception(res.json())
    return res.json()


def _request_without_token(method, url, params=None, data=None):
    base_url = "https://api.huddu.io"

    if params:
        url += "?" + parse.urlencode(params)

    s = CustomSession()

    if data:
        payload = json.dumps(data)
        res = s.request(method, f"{base_url}{url}", data=payload)
    else:
        res = s.request(method, f"{base_url}{url}")

    if res.status_code > 299:
        raise Exception(res.json())
    return res.json()
