from ..services import SecretsService

class SecretsAuditor:
    def __init__(self, region="us-east-1"):
        self.secrets_service = SecretsService(region)

    def list_all_secrets(self):
        secrets = self.secrets_service.list_secrets()
        return [{"Name": s["Name"], "ARN": s["ARN"]} for s in secrets]
