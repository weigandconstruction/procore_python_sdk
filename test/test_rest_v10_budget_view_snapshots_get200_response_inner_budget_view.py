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

from procore_sdk.models.rest_v10_budget_view_snapshots_get200_response_inner_budget_view import RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView

class TestRestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView(unittest.TestCase):
    """RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView:
        """Test RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView`
        """
        model = RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView()
        if include_optional:
            return RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView(
                id = 1234
            )
        else:
            return RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView(
        )
        """

    def testRestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView(self):
        """Test RestV10BudgetViewSnapshotsGet200ResponseInnerBudgetView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
