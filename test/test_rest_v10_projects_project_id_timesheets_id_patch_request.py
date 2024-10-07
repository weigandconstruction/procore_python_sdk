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

from procore_sdk.models.rest_v10_projects_project_id_timesheets_id_patch_request import RestV10ProjectsProjectIdTimesheetsIdPatchRequest

class TestRestV10ProjectsProjectIdTimesheetsIdPatchRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdTimesheetsIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdTimesheetsIdPatchRequest:
        """Test RestV10ProjectsProjectIdTimesheetsIdPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdTimesheetsIdPatchRequest`
        """
        model = RestV10ProjectsProjectIdTimesheetsIdPatchRequest()
        if include_optional:
            return RestV10ProjectsProjectIdTimesheetsIdPatchRequest(
                timesheet = procore_sdk.models.rest_v11_projects_project_id_project_timesheet_timecard_entries_id_patch_request_timesheet.RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatch_request_timesheet(
                    date = 'Wed Apr 19 00:00:00 UTC 2017', )
            )
        else:
            return RestV10ProjectsProjectIdTimesheetsIdPatchRequest(
                timesheet = procore_sdk.models.rest_v11_projects_project_id_project_timesheet_timecard_entries_id_patch_request_timesheet.RestV11ProjectsProjectIdProjectTimesheetTimecardEntriesIdPatch_request_timesheet(
                    date = 'Wed Apr 19 00:00:00 UTC 2017', ),
        )
        """

    def testRestV10ProjectsProjectIdTimesheetsIdPatchRequest(self):
        """Test RestV10ProjectsProjectIdTimesheetsIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
