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

from procore_sdk.models.rest_v10_budget_detail_filters_get200_response_inner import RestV10BudgetDetailFiltersGet200ResponseInner

class TestRestV10BudgetDetailFiltersGet200ResponseInner(unittest.TestCase):
    """RestV10BudgetDetailFiltersGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BudgetDetailFiltersGet200ResponseInner:
        """Test RestV10BudgetDetailFiltersGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BudgetDetailFiltersGet200ResponseInner`
        """
        model = RestV10BudgetDetailFiltersGet200ResponseInner()
        if include_optional:
            return RestV10BudgetDetailFiltersGet200ResponseInner(
                label = '01-000 - Purpose',
                value = [
                    42
                    ]
            )
        else:
            return RestV10BudgetDetailFiltersGet200ResponseInner(
        )
        """

    def testRestV10BudgetDetailFiltersGet200ResponseInner(self):
        """Test RestV10BudgetDetailFiltersGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
