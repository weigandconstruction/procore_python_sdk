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

from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_plan_template_item_assignees_inner_verification_method import RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod

class TestRestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod(unittest.TestCase):
    """RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod:
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod`
        """
        model = RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod()
        if include_optional:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod(
                id = 21,
                active = True,
                name = 'Hold Point',
                source_key = 'hold_point'
            )
        else:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod(
        )
        """

    def testRestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod(self):
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
