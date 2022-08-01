from dashboards import Dashboards


class APIClient:
    def __init__(self, token: str) -> None:
        self.token = token

        self.dashboards = Dashboards(self.token)