import boto3

class IAMService:
    def __init__(self):
        self.client = boto3.client("iam")

    def list_users(self):
        response = self.client.list_users()
        return response.get("Users", [])

    def list_user_mfa(self, user_name):
        response = self.client.list_mfa_devices(UserName=user_name)
        return response.get("MFADevices", [])

    def list_access_keys(self, user_name):
        response = self.client.list_access_keys(UserName=user_name)
        return response.get("AccessKeyMetadata", [])
