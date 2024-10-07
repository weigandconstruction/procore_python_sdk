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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_references_post_request import RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest

class TestRestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest:
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest(
                plan_template_reference = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_references_post_request_plan_template_reference.RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPost_request_plan_template_reference(
                    plan_template_item_id = 54, 
                    type = 'specification_section', 
                    payload = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_references_post_request_plan_template_reference_payload.RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPost_request_plan_template_reference_payload(
                        drawing_revision_id = 53, 
                        file_version_id = 54, 
                        specification_section_id = 55, 
                        generic_tool_item_id = 56, 
                        form_id = 57, 
                        image_id = 60, 
                        meeting_id = 58, 
                        observation_item_id = 59, ), )
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest(
                plan_template_reference = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_references_post_request_plan_template_reference.RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPost_request_plan_template_reference(
                    plan_template_item_id = 54, 
                    type = 'specification_section', 
                    payload = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_references_post_request_plan_template_reference_payload.RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPost_request_plan_template_reference_payload(
                        drawing_revision_id = 53, 
                        file_version_id = 54, 
                        specification_section_id = 55, 
                        generic_tool_item_id = 56, 
                        form_id = 57, 
                        image_id = 60, 
                        meeting_id = 58, 
                        observation_item_id = 59, ), ),
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
