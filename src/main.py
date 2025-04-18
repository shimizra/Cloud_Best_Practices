from auditors import EC2Auditor, IAMAuditor, SecretsAuditor
from reports import ConsoleReporter, JSONReporter

# Audit
ec2_auditor = EC2Auditor()
iam_auditor = IAMAuditor()
secrets_auditor = SecretsAuditor()

findings = {
    "EC2": ec2_auditor.find_public_instances_with_ssh_open(),
    "IAM": iam_auditor.find_users_without_mfa(),
    "Secrets": secrets_auditor.list_all_secrets()
}

# Report
reporter = ConsoleReporter()
reporter.report(findings)

json_reporter = JSONReporter()
json_reporter.report(findings)
