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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_manager import RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager

class TestRestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager:
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager(
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
                    name = 'Freddie's Excavating', )
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
