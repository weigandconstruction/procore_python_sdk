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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_record_requests_bulk_create_post_request import RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest

class TestRestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest:
        """Test RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest(
                plan_test_record_requests = [
                    procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_record_requests_post_request_plan_test_record_request.RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsPost_request_plan_test_record_request(
                        plan_item_id = 42, 
                        type = 'checklist', 
                        payload = procore_sdk.models.action_plan_template_references_inner_payload.Action_Plan_Template_References_inner_payload(
                            checklist_template_id = 42, 
                            form_template_id = 43, 
                            generic_tool_id = 41, ), )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest(
                plan_test_record_requests = [
                    procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_record_requests_post_request_plan_test_record_request.RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsPost_request_plan_test_record_request(
                        plan_item_id = 42, 
                        type = 'checklist', 
                        payload = procore_sdk.models.action_plan_template_references_inner_payload.Action_Plan_Template_References_inner_payload(
                            checklist_template_id = 42, 
                            form_template_id = 43, 
                            generic_tool_id = 41, ), )
                    ],
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanTestRecordRequestsBulkCreatePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
