from ..services import EC2Service

class EC2Auditor:
    def __init__(self, region):
        self.ec2_service = EC2Service(region)

    def find_public_instances_with_ssh_open(self):
        findings = []
        instances = self.ec2_service.get_all_instances()
        security_groups = self.ec2_service.get_security_groups()

        # Map SG ID to its open ports
        sg_map = {sg["GroupId"]: sg for sg in security_groups}

        for instance in instances:
            public_ip = instance.get("PublicIpAddress")
            if not public_ip:
                continue

            instance_id = instance["InstanceId"]
            for sg in instance.get("SecurityGroups", []):
                sg_id = sg["GroupId"]
                sg_data = sg_map.get(sg_id, {})
                for permission in sg_data.get("IpPermissions", []):
                    if permission.get("FromPort") == 22:
                        for ip_range in permission.get("IpRanges", []):
                            if ip_range.get("CidrIp") == "0.0.0.0/0":
                                findings.append({
                                    "InstanceId": instance_id,
                                    "PublicIp": public_ip,
                                    "SecurityGroupId": sg_id,
                                    "Issue": "SSH open to the world"
                                })
        return findings

