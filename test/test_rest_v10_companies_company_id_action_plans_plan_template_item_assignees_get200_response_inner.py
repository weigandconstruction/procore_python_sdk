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

from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_item_assignees_get200_response_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner

class TestRestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner(unittest.TestCase):
    """RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner:
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner`
        """
        model = RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner()
        if include_optional:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner(
                id = 43584,
                plan_template_item_id = 429,
                created_at = '2018-09-20T21:39:40Z',
                is_holding = True,
                plan_template_id = 248,
                role = 'architect',
                updated_at = '2018-09-20T21:39:40Z',
                verification_method = procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post_201_response_plan_template_item_assignees_inner_verification_method.RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost_201_response_plan_template_item_assignees_inner_verification_method(
                    id = 21, 
                    active = True, 
                    name = 'Hold Point', 
                    source_key = 'hold_point', )
            )
        else:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner(
        )
        """

    def testRestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner(self):
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
