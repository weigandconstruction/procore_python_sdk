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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner

class TestRestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner:
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner(
                id = 123,
                is_holding = True,
                errors = None,
                role = 'architect',
                verification_method_id = 1,
                party_id = 27,
                status = 'success'
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
