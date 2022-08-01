from connection import Connection


class Dashboards(Connection):

    def create(self, name: str, project_id: str, tags: list = [], description: str = "", meta: dict = {}) -> None:
        _, status_code = self.post("/dashboards", {
            "name": name,
            "project": project_id,
            "tags": tags,
            "description": description,
            "meta": meta
        })
        if status_code != 200:
            self.exception()
