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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request_plan_item_assignee import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee

class TestRestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee:
        """Test RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee(
                is_holding = True,
                party_id = 27,
                verification_method_id = 1
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequestPlanItemAssignee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
