from huddu.connection import Connection


class Series(Connection):

    def create(self, dashboard_id: str, name: str, description: str = "", meta: dict = {}) -> None:
        return self.post("/series", {
            "name": name,
            "dashboard": dashboard_id,
            "description": description,
            "meta": meta
        })
