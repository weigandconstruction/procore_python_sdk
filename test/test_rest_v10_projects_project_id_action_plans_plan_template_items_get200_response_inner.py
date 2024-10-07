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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner

class TestRestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner(
                id = 43584,
                plan_template_item_assignees = [
                    procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_get_200_response_inner_plan_template_item_assignees_inner.RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet_200_response_inner_plan_template_item_assignees_inner(
                        id = 43584, 
                        created_at = '2018-09-20T21:39:40Z', 
                        is_holding = True, 
                        party = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get_200_response_inner_manager.RestV10ProjectsProjectIdActionPlansPlanTemplatesGet_200_response_inner_manager(
                            id = 23, 
                            first_name = 'Paul', 
                            last_name = 'Admin', 
                            name = 'Paul Admin', 
                            user_id = 453, 
                            is_employee = True, 
                            employee_id = '12', 
                            login = 'login@example.com', 
                            updated_at = '2018-09-20T21:39:40Z', 
                            vendor = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get_200_response_inner_manager_vendor.RestV10ProjectsProjectIdActionPlansPlanTemplatesGet_200_response_inner_manager_vendor(
                                id = 223, 
                                name = 'Freddie's Excavating', ), ), 
                        role = 'architect', 
                        updated_at = '2018-09-20T21:39:40Z', 
                        verification_method = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_get_200_response_inner_plan_template_item_assignees_inner_verification_method.RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet_200_response_inner_plan_template_item_assignees_inner_verification_method(
                            id = 21, 
                            active = True, 
                            name = 'Hold Point', 
                            source_key = 'hold_point', ), )
                    ],
                created_at = '2018-09-20T21:39:40Z',
                due_at = '2018-09-20T21:39:40Z',
                description = 'A New Project Action Plan Template Item Description',
                holding_type = 'plan',
                plan_template_id = 43584,
                position = 3,
                plan_template_section_id = 43584,
                title = 'A New Project Action Plan Template Item',
                updated_at = '2018-09-20T21:39:40Z'
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
