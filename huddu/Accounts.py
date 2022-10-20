from huddu.utils import _request


class Accounts:
    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, account_id):
        return _request(self.api_key, "GET", f"/accounts/{account_id}")
