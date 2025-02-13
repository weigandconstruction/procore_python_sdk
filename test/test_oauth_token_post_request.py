# coding: utf-8

"""
    Procore Rest API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Contact: apisupport@procore.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from procore_sdk.models.oauth_token_post_request import OauthTokenPostRequest

class TestOauthTokenPostRequest(unittest.TestCase):
    """OauthTokenPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OauthTokenPostRequest:
        """Test OauthTokenPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OauthTokenPostRequest`
        """
        model = OauthTokenPostRequest()
        if include_optional:
            return OauthTokenPostRequest(
                grant_type = 'authorization_code',
                client_id = 'db0d63cfa7ac3ceed7166081542216ec99e12341300e5e879105e36bd76dbf63',
                client_secret = '0b57e8d87e35370307ba5f98ad456bd155cabacea56d49994afe083e2eb04b54',
                code = '8957b84a67f6ae55ab79c9767836a0af30b7fb7e4c36b27434993123cce71ec7',
                redirect_uri = 'http://localhost',
                refresh_token = ''
            )
        else:
            return OauthTokenPostRequest(
                grant_type = 'authorization_code',
                client_id = 'db0d63cfa7ac3ceed7166081542216ec99e12341300e5e879105e36bd76dbf63',
                client_secret = '0b57e8d87e35370307ba5f98ad456bd155cabacea56d49994afe083e2eb04b54',
        )
        """

    def testOauthTokenPostRequest(self):
        """Test OauthTokenPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
