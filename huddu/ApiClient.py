from huddu.Accounts import Accounts
from huddu.Events import Events
from huddu.Projects import Projects
from huddu.Streams import Streams


class HudduClientException(Exception):
    pass


class ApiClient:
    def __init__(self, api_key):
        """
        The main client for posting events to the huddu platform.
        :param project:
        :param stream:
        """
        self.base_url = "https://api.huddu.io"
        self.Projects = Projects(api_key)
        self.Accounts = Accounts(api_key)
        self.Streams = Streams(api_key)
        self.Events = Events(api_key)
