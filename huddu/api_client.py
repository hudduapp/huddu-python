from huddu.dashboards import Dashboards
from huddu.entries import Entries
from huddu.series import Series


class APIClient:
    def __init__(self, token: str) -> None:
        self.token = token

        self.dashboards = Dashboards(self.token)
        self.series = Series(self.token)
        self.entries = Entries(self.token)
