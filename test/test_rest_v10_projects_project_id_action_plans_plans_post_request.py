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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_post_request import RestV10ProjectsProjectIdActionPlansPlansPostRequest

class TestRestV10ProjectsProjectIdActionPlansPlansPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlansPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlansPostRequest:
        """Test RestV10ProjectsProjectIdActionPlansPlansPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlansPostRequest`
        """
        model = RestV10ProjectsProjectIdActionPlansPlansPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlansPostRequest(
                plan = procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_post_request_plan.RestV10ProjectsProjectIdActionPlansPlansPost_request_plan(
                    title = 'A new Action Plan', 
                    description = 'A description of the Action Plan', 
                    private = False, 
                    location_id = 4, 
                    manager_id = 43, 
                    plan_type_id = 2, 
                    plan_approvers_attributes = [
                        procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_post_request_plan_plan_approvers_attributes_inner.RestV10ProjectsProjectIdActionPlansPlansPost_request_plan_plan_approvers_attributes_inner(
                            party_id = 56, )
                        ], 
                    plan_receivers_attributes = [
                        procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_post_request_plan_plan_receivers_attributes_inner.RestV10ProjectsProjectIdActionPlansPlansPost_request_plan_plan_receivers_attributes_inner(
                            party_id = 56, )
                        ], 
                    custom_field_%{custom_field_definition_id} = custom field value, )
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlansPostRequest(
                plan = procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_post_request_plan.RestV10ProjectsProjectIdActionPlansPlansPost_request_plan(
                    title = 'A new Action Plan', 
                    description = 'A description of the Action Plan', 
                    private = False, 
                    location_id = 4, 
                    manager_id = 43, 
                    plan_type_id = 2, 
                    plan_approvers_attributes = [
                        procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_post_request_plan_plan_approvers_attributes_inner.RestV10ProjectsProjectIdActionPlansPlansPost_request_plan_plan_approvers_attributes_inner(
                            party_id = 56, )
                        ], 
                    plan_receivers_attributes = [
                        procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_post_request_plan_plan_receivers_attributes_inner.RestV10ProjectsProjectIdActionPlansPlansPost_request_plan_plan_receivers_attributes_inner(
                            party_id = 56, )
                        ], 
                    custom_field_%{custom_field_definition_id} = custom field value, ),
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlansPostRequest(self):
        """Test RestV10ProjectsProjectIdActionPlansPlansPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
