from huddu.utils import _request_without_token


class Integrations:
    def __init__(self, integration):
        self.integration = integration

    def authorize(self, secret: str, code: str) -> dict:
        return _request_without_token(
            "POST",
            f"/integrations/{self.integration}/authorize",
            data={
                "secret": secret,
                "code": code
            },
        )

    def refresh_token(self, token: str, refresh_token: str) -> dict:
        return _request_without_token(
            "POST",
            f"/integrations/{self.integration}/refresh_token",
            data={
                "token": token,
                "refresh_token": refresh_token
            },
        )
