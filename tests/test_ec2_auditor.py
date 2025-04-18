from src.auditors.ec2_auditor import EC2Auditor

def test_find_public_instances_with_ssh_open():
    ec2 = EC2Auditor(region="us-east-1")
    res = ec2.find_public_instances_with_ssh_open()

    assert res is not None

    print(f'\nResults: Counts:{len(res)}\n{res}')
