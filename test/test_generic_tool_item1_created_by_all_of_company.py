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

from procore_sdk.models.generic_tool_item1_created_by_all_of_company import GenericToolItem1CreatedByAllOfCompany

class TestGenericToolItem1CreatedByAllOfCompany(unittest.TestCase):
    """GenericToolItem1CreatedByAllOfCompany unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericToolItem1CreatedByAllOfCompany:
        """Test GenericToolItem1CreatedByAllOfCompany
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericToolItem1CreatedByAllOfCompany`
        """
        model = GenericToolItem1CreatedByAllOfCompany()
        if include_optional:
            return GenericToolItem1CreatedByAllOfCompany(
                id = 160583,
                name = 'Company ABC'
            )
        else:
            return GenericToolItem1CreatedByAllOfCompany(
        )
        """

    def testGenericToolItem1CreatedByAllOfCompany(self):
        """Test GenericToolItem1CreatedByAllOfCompany"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
