import boto3

class SecretsService:
    def __init__(self, region_name="us-east-1"):  # TODO Region is hardcoded
        self.client = boto3.client("secretsmanager", region_name=region_name)

    def list_secrets(self):
        paginator = self.client.get_paginator("list_secrets")
        secrets = []
        for page in paginator.paginate():
            secrets.extend(page.get("SecretList", []))
        return secrets


    # TODO You can later add filtering, like unused/never accessed, etc.
