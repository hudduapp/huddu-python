from huddu import HudduClient


class Interceptor:
    def __init__(self):
        self.client = _make_client()
        _apply_patches()
        _run()

    def _make_client(self) -> HudduClient:
        raise NotImplementedError

    def _get_client(self):
        return self.client

    def _apply_patches(self):
        raise NotImplementedError

    def _run(self):
        pass
