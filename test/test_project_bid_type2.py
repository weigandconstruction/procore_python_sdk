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

from procore_sdk.models.project_bid_type2 import ProjectBidType2

class TestProjectBidType2(unittest.TestCase):
    """ProjectBidType2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectBidType2:
        """Test ProjectBidType2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectBidType2`
        """
        model = ProjectBidType2()
        if include_optional:
            return ProjectBidType2(
                id = 1,
                name = 'Negotiated'
            )
        else:
            return ProjectBidType2(
        )
        """

    def testProjectBidType2(self):
        """Test ProjectBidType2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
