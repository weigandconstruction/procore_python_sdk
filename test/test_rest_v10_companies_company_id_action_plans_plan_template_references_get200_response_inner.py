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

from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_references_get200_response_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner

class TestRestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner(unittest.TestCase):
    """RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner:
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner`
        """
        model = RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner()
        if include_optional:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner(
                id = 12,
                plan_template_item_id = 54,
                created_at = '2018-09-20T21:39:40Z',
                payload = procore_sdk.models.rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get_200_response_inner_payload.RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet_200_response_inner_payload(
                    attachment = procore_sdk.models.rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get_200_response_inner_payload_attachment.RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet_200_response_inner_payload_attachment(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        thumbnail_url = 'http://www.example.com/', 
                        name = 'january_receipt_copy.jpg', 
                        content_type = 'image/jpg', ), ),
                plan_template_id = 985,
                type = 'attachment',
                updated_at = '2018-09-20T21:39:40Z'
            )
        else:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner(
        )
        """

    def testRestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner(self):
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
