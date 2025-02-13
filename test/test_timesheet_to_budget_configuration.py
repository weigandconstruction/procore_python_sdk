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

from procore_sdk.models.timesheet_to_budget_configuration import TimesheetToBudgetConfiguration

class TestTimesheetToBudgetConfiguration(unittest.TestCase):
    """TimesheetToBudgetConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimesheetToBudgetConfiguration:
        """Test TimesheetToBudgetConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimesheetToBudgetConfiguration`
        """
        model = TimesheetToBudgetConfiguration()
        if include_optional:
            return TimesheetToBudgetConfiguration(
                id = 1,
                line_item_type_id = 8,
                erp_default_line_item_type_id = 12,
                company_id = 13,
                has_backfilled = False
            )
        else:
            return TimesheetToBudgetConfiguration(
        )
        """

    def testTimesheetToBudgetConfiguration(self):
        """Test TimesheetToBudgetConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
