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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch_request import RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest

class TestRestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest:
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest(
                plan_template_item_assignees = [
                    procore_sdk.models.action_plan_template_item_assignees_inner_1.Action_Plan_Template_Item_Assignees_inner_1(
                        id = 123, 
                        is_holding = True, 
                        party_id = 27, 
                        role = 'architect', 
                        verification_method_id = 1, )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest(
                plan_template_item_assignees = [
                    procore_sdk.models.action_plan_template_item_assignees_inner_1.Action_Plan_Template_Item_Assignees_inner_1(
                        id = 123, 
                        is_holding = True, 
                        party_id = 27, 
                        role = 'architect', 
                        verification_method_id = 1, )
                    ],
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
