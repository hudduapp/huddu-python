import json
from urllib import request, parse


def _request(api_key, method, url, params=None, data=None):
    headers = {"Authorization": f"Token {api_key}", "OtherHeader": "hey"}
    base_url = "https://api.huddu.io"

    req_url = f"{base_url}{url}"
    if params:
        req_url += "?" + parse.urlencode(params)
        r = request.Request(req_url, data=data, headers=headers, method=method)
    elif data:
        r = request.Request(req_url, headers=headers, method=method)
    else:
        r = request.Request(req_url, headers=headers, method=method)

    res = request.urlopen(r)

    if res.getcode() > 299:
        raise Exception(json.loads(res.read().decode("utf-8")))
    else:
        return json.loads(res.read().decode("utf-8"))
