from huddu.connection import Connection


class Entries(Connection):

    def create(self, series_id: str, data: dict = {}, meta: dict = {}) -> None:
        return self.post("/entries", {
            "series": series_id,
            "data": data,
            "meta": meta
        })
