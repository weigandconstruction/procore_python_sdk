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

from procore_sdk.models.rest_v10_projects_project_id_daily_construction_report_logs_id_patch_request_daily_construction_report_log import RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog

class TestRestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog(unittest.TestCase):
    """RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog:
        """Test RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog`
        """
        model = RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog()
        if include_optional:
            return RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog(
                apprentice_hours = '3.0',
                var_date = 'Thu May 19 00:00:00 UTC 2016',
                datetime = '2016-05-19T12:00Z',
                first_year_hours = '3.5',
                foreman_hours = '1.0',
                journeyman_hours = '2.0',
                local_city_hours = '3.5',
                local_county_hours = '3.5',
                minority_hours = '3.5',
                notes = 'No other workers on site today',
                number_of_apprentice_workers = 4,
                number_of_foreman_workers = 3,
                number_of_journeyman_workers = 4,
                number_of_other_workers = 5,
                other_hours = '4.0',
                vendor_id = 1120327,
                status = 'approved',
                trade_id = 100884,
                veteran_hours = '3.5',
                women_hours = '3.5',
                custom_field_custom_field_definition_id = custom field value
            )
        else:
            return RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog(
        )
        """

    def testRestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog(self):
        """Test RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequestDailyConstructionReportLog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
