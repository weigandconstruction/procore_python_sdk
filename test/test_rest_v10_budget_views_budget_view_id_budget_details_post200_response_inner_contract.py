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

from procore_sdk.models.rest_v10_budget_views_budget_view_id_budget_details_post200_response_inner_contract import RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract

class TestRestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract(unittest.TestCase):
    """RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract:
        """Test RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract`
        """
        model = RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract()
        if include_optional:
            return RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract(
                id = 123,
                name = 'Framing Subcontract'
            )
        else:
            return RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract(
        )
        """

    def testRestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract(self):
        """Test RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInnerContract"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
