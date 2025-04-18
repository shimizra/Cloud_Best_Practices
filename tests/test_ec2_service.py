from src.services.ec2_service import EC2Service

def test_list_instances():
    ec2 = EC2Service(region_name="us-east-1")
    instances = ec2.get_all_instances()

    assert len(instances) > 0

    print(f'\ninstances: {instances}')

def test_list_sg():
    ec2 = EC2Service(region_name="us-east-1")
    sg = ec2.get_security_groups()

    assert len(sg) > 0

    print(f'\nSG: {sg}')


