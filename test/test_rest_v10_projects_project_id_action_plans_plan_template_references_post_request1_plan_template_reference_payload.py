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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_references_post_request1_plan_template_reference_payload import RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload

class TestRestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload:
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload(
                drawing_revision_id = 53,
                file_version_id = 54,
                specification_section_id = 55,
                attachment = bytes(b'blah'),
                generic_tool_item_id = 56,
                form_id = 57,
                image_id = 60,
                meeting_id = 58,
                observation_item_id = 59
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateReferencesPostRequest1PlanTemplateReferencePayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
