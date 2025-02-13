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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_receivers_inner_signature import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature

class TestRestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature:
        """Test RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature`
        """
        model = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature(
                id = 32,
                attachment = procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get_200_response_inner_plan_approvers_inner_signature_attachment.RestV10ProjectsProjectIdActionPlansPlansGet_200_response_inner_plan_approvers_inner_signature_attachment(
                    id = 23, 
                    content_type = 'image/png', 
                    name = 'image.png', 
                    url = '', ),
                captured_at = '2015-02-07T00:00Z',
                captured_by = procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get_200_response_inner_plan_approvers_inner_signature_captured_by.RestV10ProjectsProjectIdActionPlansPlansGet_200_response_inner_plan_approvers_inner_signature_captured_by(
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
                    updated_at = '2017-01-04T21:27:18Z', )
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature(self):
        """Test RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInnerSignature"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
