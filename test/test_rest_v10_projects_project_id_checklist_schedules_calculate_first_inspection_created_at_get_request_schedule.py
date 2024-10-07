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

from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request_schedule import RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule

class TestRestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule(unittest.TestCase):
    """RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule:
        """Test RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule`
        """
        model = RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule()
        if include_optional:
            return RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule(
                starts_at = '2019-10-27T07:40:12Z',
                ends_at = '2019-10-27T07:40:12Z',
                frequency = 'once_every_two_weeks',
                days_created_before_due_date = 3
            )
        else:
            return RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule(
                starts_at = '2019-10-27T07:40:12Z',
                ends_at = '2019-10-27T07:40:12Z',
                frequency = 'once_every_two_weeks',
                days_created_before_due_date = 3,
        )
        """

    def testRestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule(self):
        """Test RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
