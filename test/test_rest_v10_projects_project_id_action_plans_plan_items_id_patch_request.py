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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_id_patch_request import RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest

class TestRestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest:
        """Test RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest(
                plan_item = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_id_patch_request_plan_item.RestV10ProjectsProjectIdActionPlansPlanItemsIdPatch_request_plan_item(
                    title = 'A new Action Plan Item', 
                    description = 'Must perform the 2 items for the Action Plan Item', 
                    notes = 'Noting this Action Plan Item is complete', 
                    due_at = '2017-07-29T21:39:40Z', 
                    holding_type = 'section', 
                    status_id = 2, )
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest(
                plan_item = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_id_patch_request_plan_item.RestV10ProjectsProjectIdActionPlansPlanItemsIdPatch_request_plan_item(
                    title = 'A new Action Plan Item', 
                    description = 'Must perform the 2 items for the Action Plan Item', 
                    notes = 'Noting this Action Plan Item is complete', 
                    due_at = '2017-07-29T21:39:40Z', 
                    holding_type = 'section', 
                    status_id = 2, ),
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
