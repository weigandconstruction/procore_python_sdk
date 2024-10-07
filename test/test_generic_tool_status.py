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

from procore_sdk.models.generic_tool_status import GenericToolStatus

class TestGenericToolStatus(unittest.TestCase):
    """GenericToolStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericToolStatus:
        """Test GenericToolStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericToolStatus`
        """
        model = GenericToolStatus()
        if include_optional:
            return GenericToolStatus(
                status_name = 'In Review',
                status = 'Open'
            )
        else:
            return GenericToolStatus(
                status_name = 'In Review',
                status = 'Open',
        )
        """

    def testGenericToolStatus(self):
        """Test GenericToolStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
