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

from procore_sdk.models.rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request import RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest

class TestRestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest(unittest.TestCase):
    """RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest:
        """Test RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest`
        """
        model = RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest()
        if include_optional:
            return RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest(
                requested_change = procore_sdk.models.rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request_requested_change.RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPost_request_requested_change(
                    change_reason = 'Change schedule request', 
                    other_change = 'Other change', 
                    task = procore_sdk.models.rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request_requested_change_task.RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPost_request_requested_change_task(
                        start = '2022-01-31', 
                        finish = '2022-02-15', 
                        percentage = 50, ), 
                    notes = 'Delayed due to weather', )
            )
        else:
            return RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest(
        )
        """

    def testRestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest(self):
        """Test RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
