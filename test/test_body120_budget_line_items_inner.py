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

from procore_sdk.models.body120_budget_line_items_inner import Body120BudgetLineItemsInner

class TestBody120BudgetLineItemsInner(unittest.TestCase):
    """Body120BudgetLineItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body120BudgetLineItemsInner:
        """Test Body120BudgetLineItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body120BudgetLineItemsInner`
        """
        model = Body120BudgetLineItemsInner()
        if include_optional:
            return Body120BudgetLineItemsInner(
                wbs_code_id = 67890,
                original_budget_amount = 10000.00,
                uom = 'hours',
                quantity = 250.5,
                unit_cost = 123.5,
                calculation_strategy = 'manual',
                id = 1232
            )
        else:
            return Body120BudgetLineItemsInner(
                wbs_code_id = 67890,
        )
        """

    def testBody120BudgetLineItemsInner(self):
        """Test Body120BudgetLineItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
