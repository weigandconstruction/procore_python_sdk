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

from procore_sdk.models.generic_tool_item1_created_by import GenericToolItem1CreatedBy

class TestGenericToolItem1CreatedBy(unittest.TestCase):
    """GenericToolItem1CreatedBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericToolItem1CreatedBy:
        """Test GenericToolItem1CreatedBy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericToolItem1CreatedBy`
        """
        model = GenericToolItem1CreatedBy()
        if include_optional:
            return GenericToolItem1CreatedBy(
                id = 160586,
                login = 'carl.contractor@example.com',
                name = 'Carl Contractor',
                company = procore_sdk.models.generic_tool_item_1_created_by_all_of_company.GenericToolItem_1_created_by_allOf_company(
                    id = 160583, 
                    name = 'Company ABC', )
            )
        else:
            return GenericToolItem1CreatedBy(
        )
        """

    def testGenericToolItem1CreatedBy(self):
        """Test GenericToolItem1CreatedBy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
