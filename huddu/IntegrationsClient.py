from huddu.Integrations import Integrations


class IntegrationsClient:
    def __init__(self, integration_id):
        self.Integrations = Integrations(integration_id)
