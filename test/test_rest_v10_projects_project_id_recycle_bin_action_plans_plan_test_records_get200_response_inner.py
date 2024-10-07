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

from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner

class TestRestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner(
                id = 12,
                plan_item_id = 54,
                created_at = '2018-09-20T21:39:40Z',
                deleted_at = '2019-10-25T18:46:40Z',
                payload = procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get_200_response_inner_payload.RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet_200_response_inner_payload(
                    checklist_id = 55, 
                    checklist_template_id = 42, 
                    attachment = procore_sdk.models.rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get_200_response_inner_payload_attachment.RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet_200_response_inner_payload_attachment(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        thumbnail_url = 'http://www.example.com/', 
                        name = 'january_receipt_copy.jpg', 
                        content_type = 'image/jpg', ), ),
                plan_id = 985,
                plan_test_record_request_id = 42,
                type = 'checklist',
                updated_at = '2018-09-20T21:39:40Z'
            )
        else:
            return RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
