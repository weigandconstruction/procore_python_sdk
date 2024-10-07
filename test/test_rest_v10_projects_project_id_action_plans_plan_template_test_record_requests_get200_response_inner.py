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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner

class TestRestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner(
                id = 12,
                plan_template_item_id = 54,
                created_at = '2018-09-20T21:39:40Z',
                payload = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get_200_response_inner_payload.RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet_200_response_inner_payload(
                    checklist_template_id = 55, ),
                plan_template_id = 985,
                type = 'checklist',
                updated_at = '2018-09-20T21:39:40Z'
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
