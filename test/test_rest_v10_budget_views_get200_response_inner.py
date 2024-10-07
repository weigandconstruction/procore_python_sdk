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

from procore_sdk.models.rest_v10_budget_views_get200_response_inner import RestV10BudgetViewsGet200ResponseInner

class TestRestV10BudgetViewsGet200ResponseInner(unittest.TestCase):
    """RestV10BudgetViewsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BudgetViewsGet200ResponseInner:
        """Test RestV10BudgetViewsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BudgetViewsGet200ResponseInner`
        """
        model = RestV10BudgetViewsGet200ResponseInner()
        if include_optional:
            return RestV10BudgetViewsGet200ResponseInner(
                id = 75414,
                name = 'Procore Standard View',
                description = 'This is the procore standard view',
                created_at = '2018-01-17T18:09:03Z',
                created_by = procore_sdk.models.rest_v10_budget_views_get_200_response_inner_created_by.RestV10BudgetViewsGet_200_response_inner_created_by(
                    id = 1234, 
                    name = 'John Doe', 
                    login = 'john.doe@example.com', ),
                updated_at = '2018-01-17T18:09:03Z',
                role = 'forecasting',
                links = procore_sdk.models.rest_v10_budget_views_get_200_response_inner_links.RestV10BudgetViewsGet_200_response_inner_links(
                    detail_rows = 'https://app.procore.com/rest/v1.0/budget_views/1/detail_rows?project_id=2', 
                    summary_rows = 'https://app.procore.com/rest/v1.0/budget_views/1/summary_rows?project_id=2', )
            )
        else:
            return RestV10BudgetViewsGet200ResponseInner(
        )
        """

    def testRestV10BudgetViewsGet200ResponseInner(self):
        """Test RestV10BudgetViewsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
