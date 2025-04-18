import boto3

class EC2Service:
    def __init__(self, region_name):
        self.ec2_client = boto3.client("ec2", region_name=region_name)

    def get_all_instances(self):
        instances = []
        paginator = self.ec2_client.get_paginator("describe_instances")
        for page in paginator.paginate():
            for reservation in page.get("Reservations", []):
                for instance in reservation.get("Instances", []):
                    instances.append(instance)
        return instances

    def get_security_groups(self):
        response = self.ec2_client.describe_security_groups()
        return response.get("SecurityGroups", [])
