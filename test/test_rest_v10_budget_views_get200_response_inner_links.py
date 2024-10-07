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

from procore_sdk.models.rest_v10_budget_views_get200_response_inner_links import RestV10BudgetViewsGet200ResponseInnerLinks

class TestRestV10BudgetViewsGet200ResponseInnerLinks(unittest.TestCase):
    """RestV10BudgetViewsGet200ResponseInnerLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BudgetViewsGet200ResponseInnerLinks:
        """Test RestV10BudgetViewsGet200ResponseInnerLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BudgetViewsGet200ResponseInnerLinks`
        """
        model = RestV10BudgetViewsGet200ResponseInnerLinks()
        if include_optional:
            return RestV10BudgetViewsGet200ResponseInnerLinks(
                detail_rows = 'https://app.procore.com/rest/v1.0/budget_views/1/detail_rows?project_id=2',
                summary_rows = 'https://app.procore.com/rest/v1.0/budget_views/1/summary_rows?project_id=2'
            )
        else:
            return RestV10BudgetViewsGet200ResponseInnerLinks(
        )
        """

    def testRestV10BudgetViewsGet200ResponseInnerLinks(self):
        """Test RestV10BudgetViewsGet200ResponseInnerLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
