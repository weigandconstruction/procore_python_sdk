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

from procore_sdk.models.rest_v10_project_project_id_email_communications_id_patch_request import RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest

class TestRestV10ProjectProjectIdEmailCommunicationsIdPatchRequest(unittest.TestCase):
    """RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest:
        """Test RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest`
        """
        model = RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest()
        if include_optional:
            return RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest(
                private = True
            )
        else:
            return RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest(
                private = True,
        )
        """

    def testRestV10ProjectProjectIdEmailCommunicationsIdPatchRequest(self):
        """Test RestV10ProjectProjectIdEmailCommunicationsIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
