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

from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner

class TestRestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner(unittest.TestCase):
    """RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner:
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner`
        """
        model = RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner()
        if include_optional:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner(
                plan_template_item_id = 42,
                type = 'checklist',
                payload = procore_sdk.models.action_plan_template_references_inner_payload.Action_Plan_Template_References_inner_payload(
                    checklist_template_id = 42, 
                    form_template_id = 43, 
                    generic_tool_id = 41, ),
                status = 'success',
                errors = None
            )
        else:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner(
        )
        """

    def testRestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner(self):
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
