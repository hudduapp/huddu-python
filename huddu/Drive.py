import time

from ._sessions import Session


class Drive:
    def __init__(
        self,
        token: str,
        collection: str,
        region: str,
        base_url: str = "https://connect.huddu.io",
    ):
        self.session = Session(collection, token, region, base_url)

    def upload(self, name: str, data: str = None, path: str = None):
        n = int(1e7)  # 10 MB in bytes

        if path:
            f = open(path, "r")
            data = f.read()

        chunks = [data[i : i + n] for i in range(0, len(data), n)]

        documents = []
        for i in chunks:
            documents.append({"id": f"{name}_{chunks.index(i) + 1}", "data": i})

        for i in documents:
            self.session.create_documents([i])
            time.sleep(1)

    def get(self, name: str):
        run = 1
        while True:
            try:
                document = self.session.list_documents([f"{name}_{run}"])
                yield document["data"][0]["data"]
                run += 1
            except:
                break

    def delete(self, name: str):
        run = 1
        while True:
            try:
                res = self.session.delete_documents([f"{name}_{run}"])
                if res.get("error"):
                    break
                run += 1
            except:
                break
