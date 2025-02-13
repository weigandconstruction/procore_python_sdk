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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post_request import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest

class TestRestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest:
        """Test RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest(
                plan_item_assignees = [
                    procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request_plan_item_assignee.RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPost_request_plan_item_assignee(
                        plan_item_id = 42, 
                        is_holding = True, 
                        party_id = 27, 
                        role = 'specialty_contractor', 
                        verification_method_id = 1, )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest(
                plan_item_assignees = [
                    procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request_plan_item_assignee.RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPost_request_plan_item_assignee(
                        plan_item_id = 42, 
                        is_holding = True, 
                        party_id = 27, 
                        role = 'specialty_contractor', 
                        verification_method_id = 1, )
                    ],
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
