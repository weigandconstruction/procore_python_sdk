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

from procore_sdk.models.standard_cost_code_list import StandardCostCodeList

class TestStandardCostCodeList(unittest.TestCase):
    """StandardCostCodeList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StandardCostCodeList:
        """Test StandardCostCodeList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StandardCostCodeList`
        """
        model = StandardCostCodeList()
        if include_optional:
            return StandardCostCodeList(
                available_to_use_on_new_projects = True,
                id = 12345,
                is_erp_list = True,
                name = 'Client X Cost Codes'
            )
        else:
            return StandardCostCodeList(
        )
        """

    def testStandardCostCodeList(self):
        """Test StandardCostCodeList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
