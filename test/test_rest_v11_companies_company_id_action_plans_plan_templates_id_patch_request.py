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

from procore_sdk.models.rest_v11_companies_company_id_action_plans_plan_templates_id_patch_request import RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest

class TestRestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest(unittest.TestCase):
    """RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest:
        """Test RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest`
        """
        model = RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest()
        if include_optional:
            return RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest(
                plan_template = procore_sdk.models.rest_v11_companies_company_id_action_plans_plan_templates_id_patch_request_plan_template.RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatch_request_plan_template(
                    title = 'A new Company Action Plan Template', 
                    description = 'A short description explaining what this Company Action Plan Template is supposed to do', 
                    private = False, 
                    plan_type_id = 2, )
            )
        else:
            return RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest(
                plan_template = procore_sdk.models.rest_v11_companies_company_id_action_plans_plan_templates_id_patch_request_plan_template.RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatch_request_plan_template(
                    title = 'A new Company Action Plan Template', 
                    description = 'A short description explaining what this Company Action Plan Template is supposed to do', 
                    private = False, 
                    plan_type_id = 2, ),
        )
        """

    def testRestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest(self):
        """Test RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
