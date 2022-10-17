from huddu.utils import _request


class Projects:
    def __init__(self, api_key):
        self.api_key = api_key

    def list(self, account: str, skip: int = 0, limit: int = 25):
        return _request(
            self.api_key,
            "GET",
            f"/accounts/{account}/projects",
            params={"skip": skip, "limit": limit},
        )

    def get(
        self,
        id: str,
        account: str,
    ):
        return _request(self.api_key, "GET", f"/accounts/{account}/projects/{id}")
