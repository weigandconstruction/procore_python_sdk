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

from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_record_requests_get200_response_inner_payload import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload

class TestRestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload(unittest.TestCase):
    """RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload:
        """Test RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload`
        """
        model = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload()
        if include_optional:
            return RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload(
                checklist_template_id = 55
            )
        else:
            return RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload(
        )
        """

    def testRestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload(self):
        """Test RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordRequestsGet200ResponseInnerPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
