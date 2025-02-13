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

from procore_sdk.models.rest_v10_budget_line_items_post201_response_division import RestV10BudgetLineItemsPost201ResponseDivision

class TestRestV10BudgetLineItemsPost201ResponseDivision(unittest.TestCase):
    """RestV10BudgetLineItemsPost201ResponseDivision unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BudgetLineItemsPost201ResponseDivision:
        """Test RestV10BudgetLineItemsPost201ResponseDivision
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BudgetLineItemsPost201ResponseDivision`
        """
        model = RestV10BudgetLineItemsPost201ResponseDivision()
        if include_optional:
            return RestV10BudgetLineItemsPost201ResponseDivision(
                id = 236246,
                name = 'Wood floors',
                full_code = '11-123'
            )
        else:
            return RestV10BudgetLineItemsPost201ResponseDivision(
        )
        """

    def testRestV10BudgetLineItemsPost201ResponseDivision(self):
        """Test RestV10BudgetLineItemsPost201ResponseDivision"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
