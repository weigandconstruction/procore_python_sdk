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

from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_items_bulk_update_patch200_response_inner_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner

class TestRestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner(unittest.TestCase):
    """RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner:
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner`
        """
        model = RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner()
        if include_optional:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner(
                id = 123,
                description = 'Must perform the 2 items for the Action Plan Item',
                status = 'success',
                errors = None
            )
        else:
            return RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner(
        )
        """

    def testRestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner(self):
        """Test RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
