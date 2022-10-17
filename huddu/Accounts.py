from huddu.utils import _request


class Accounts:
    def __init__(self, api_key):
        self.api_key = api_key

    def list_installations(self, skip: int = 0, limit: int = 25):
        return _request(
            self.api_key, "GET", "/installations", params={"skip": skip, "limit": limit}
        )

    def get(self, account_id):
        return _request(self.api_key, "GET", f"/accounts/{account_id}")
