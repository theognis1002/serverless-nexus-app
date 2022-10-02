import json

import boto3
import botocore

from nexus.ip.app import ip_address_handler
from nexus.ua.app import user_agent_handler
from tests.conftest import requires_mockserver


class TestMockServerEndpoints:
    """Integration Tests using AWS SAM's mock servern"""
    @requires_mockserver()
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


class TestEndpoints:
    """Integration Tests using AWS SAM's mock servern"""

    def test_ip_handler(self):
        response = ip_address_handler({}, {})
        assert response["statusCode"] == 200
        assert json.loads(response["body"])

    def test_ua_handler(self):
        response = user_agent_handler({}, {})
        assert response["statusCode"] == 200
        assert json.loads(response["body"])
