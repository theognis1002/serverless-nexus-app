import boto3
import botocore


class TestEndpoints:
    def test_nexus_endpoint(self):
        lambda_client = boto3.client('lambda',
                                     region_name="us-east-1",
                                     endpoint_url="http://127.0.0.1:3001",
                                     use_ssl=False,
                                     verify=False,
                                     config=botocore.client.Config(
                                         signature_version=botocore.UNSIGNED,
                                         read_timeout=1200,
                                         retries={'max_attempts': 0},
                                     )
                                     )

        response = lambda_client.invoke(FunctionName='NexusFunction')
        assert response["StatusCode"] == 200
