from huddu.Accounts import Accounts
from huddu.Events import Events
from huddu.Installations import Installations
from huddu.Projects import Projects
from huddu.Streams import Streams


class HudduClientException(Exception):
    pass


class ApiClient:
    def __init__(self, api_key):
        self.Projects = Projects(api_key)
        self.Accounts = Accounts(api_key)
        self.Streams = Streams(api_key)
        self.Events = Events(api_key)
        self.Installations = Installations(api_key)
