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

from procore_sdk.models.rest_v10_projects_project_id_schedule_lookahead_tasks_post_request import RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest

class TestRestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest:
        """Test RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest`
        """
        model = RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest(
                lookahead_task = procore_sdk.models.lookahead_task.Lookahead Task(
                    lookahead_id = 8, 
                    parent_id = 1, 
                    name = 'Interior', 
                    start_date = '2019-09-20', 
                    end_date = '2019-09-30', 
                    resource_ids = [
                        1
                        ], 
                    comment = '', 
                    segments = [
                        procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get_200_response_lookahead_tasks_inner_segments_inner.RestV11ProjectsProjectIdScheduleLookaheadsIdGet_200_response_lookahead_tasks_inner_segments_inner(
                            date = '2019-09-20', 
                            status = 'complete', )
                        ], 
                    assignee_ids = [
                        1
                        ], 
                    vendor_ids = [
                        1
                        ], )
            )
        else:
            return RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest(
                lookahead_task = procore_sdk.models.lookahead_task.Lookahead Task(
                    lookahead_id = 8, 
                    parent_id = 1, 
                    name = 'Interior', 
                    start_date = '2019-09-20', 
                    end_date = '2019-09-30', 
                    resource_ids = [
                        1
                        ], 
                    comment = '', 
                    segments = [
                        procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get_200_response_lookahead_tasks_inner_segments_inner.RestV11ProjectsProjectIdScheduleLookaheadsIdGet_200_response_lookahead_tasks_inner_segments_inner(
                            date = '2019-09-20', 
                            status = 'complete', )
                        ], 
                    assignee_ids = [
                        1
                        ], 
                    vendor_ids = [
                        1
                        ], ),
        )
        """

    def testRestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest(self):
        """Test RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
