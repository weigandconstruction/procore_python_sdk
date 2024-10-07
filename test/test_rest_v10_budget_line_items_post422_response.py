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

from procore_sdk.models.rest_v10_budget_line_items_post422_response import RestV10BudgetLineItemsPost422Response

class TestRestV10BudgetLineItemsPost422Response(unittest.TestCase):
    """RestV10BudgetLineItemsPost422Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BudgetLineItemsPost422Response:
        """Test RestV10BudgetLineItemsPost422Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BudgetLineItemsPost422Response`
        """
        model = RestV10BudgetLineItemsPost422Response()
        if include_optional:
            return RestV10BudgetLineItemsPost422Response(
                message = '',
                error = '422 - Unprocessable Currency'
            )
        else:
            return RestV10BudgetLineItemsPost422Response(
        )
        """

    def testRestV10BudgetLineItemsPost422Response(self):
        """Test RestV10BudgetLineItemsPost422Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
