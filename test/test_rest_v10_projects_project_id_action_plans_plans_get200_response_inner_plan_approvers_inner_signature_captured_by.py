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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_captured_by import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy

class TestRestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy:
        """Test RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy`
        """
        model = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy(
                id = 56,
                first_name = 'Paul',
                last_name = 'Admin',
                name = 'Paul Admin',
                user_id = 453,
                is_employee = True,
                employee_id = 12,
                login = 'contractor@example.com',
                vendor = procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get_200_response_inner_plan_approvers_inner_signature_captured_by_vendor.RestV10ProjectsProjectIdActionPlansPlansGet_200_response_inner_plan_approvers_inner_signature_captured_by_vendor(
                    id = 223, 
                    name = 'Freddie's Excavating', ),
                updated_at = '2017-01-04T21:27:18Z'
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy(self):
        """Test RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
