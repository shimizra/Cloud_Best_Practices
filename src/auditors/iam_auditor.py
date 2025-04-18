from ..services import IAMService

class IAMAuditor:
    def __init__(self):
        self.iam_service = IAMService()

    def find_users_without_mfa(self):
        findings = []
        users = self.iam_service.list_users()

        for user in users:
            mfa_devices = self.iam_service.list_user_mfa(user["UserName"])
            if not mfa_devices:
                findings.append({
                    "UserName": user["UserName"],
                    "Issue": "No MFA device assigned"
                })

        return findings
