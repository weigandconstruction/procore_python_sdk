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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_captured_by_vendor import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor

class TestRestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor:
        """Test RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor`
        """
        model = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor(
                id = 223,
                name = 'Freddie's Excavating'
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor(self):
        """Test RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
