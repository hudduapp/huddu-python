from huddu.connection import Connection


class Dashboards(Connection):

    def create(self, project_id: str, name: str, tags: list = [], description: str = "", meta: dict = {}) -> None:
        return self.post("/dashboards", {
            "name": name,
            "project": project_id,
            "tags": tags,
            "description": description,
            "meta": meta
        })
