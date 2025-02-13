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

from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request import RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest

class TestRestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest:
        """Test RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest`
        """
        model = RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest()
        if include_optional:
            return RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest(
                schedule = procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request_schedule.RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGet_request_schedule(
                    starts_at = '2019-10-27T07:40:12Z', 
                    ends_at = '2019-10-27T07:40:12Z', 
                    frequency = 'once_every_two_weeks', 
                    days_created_before_due_date = 3, )
            )
        else:
            return RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest(
                schedule = procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request_schedule.RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGet_request_schedule(
                    starts_at = '2019-10-27T07:40:12Z', 
                    ends_at = '2019-10-27T07:40:12Z', 
                    frequency = 'once_every_two_weeks', 
                    days_created_before_due_date = 3, ),
        )
        """

    def testRestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest(self):
        """Test RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
