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

from procore_sdk.models.rest_v10_budget_line_items_post201_response_line_item_type import RestV10BudgetLineItemsPost201ResponseLineItemType

class TestRestV10BudgetLineItemsPost201ResponseLineItemType(unittest.TestCase):
    """RestV10BudgetLineItemsPost201ResponseLineItemType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BudgetLineItemsPost201ResponseLineItemType:
        """Test RestV10BudgetLineItemsPost201ResponseLineItemType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BudgetLineItemsPost201ResponseLineItemType`
        """
        model = RestV10BudgetLineItemsPost201ResponseLineItemType()
        if include_optional:
            return RestV10BudgetLineItemsPost201ResponseLineItemType(
                id = 23107,
                name = 'Equipment'
            )
        else:
            return RestV10BudgetLineItemsPost201ResponseLineItemType(
        )
        """

    def testRestV10BudgetLineItemsPost201ResponseLineItemType(self):
        """Test RestV10BudgetLineItemsPost201ResponseLineItemType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
