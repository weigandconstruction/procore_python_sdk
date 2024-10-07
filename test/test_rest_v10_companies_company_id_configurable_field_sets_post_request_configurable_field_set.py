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

from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set import RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet

class TestRestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet(unittest.TestCase):
    """RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet:
        """Test RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet`
        """
        model = RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet()
        if include_optional:
            return RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet(
                name = 'Observation Form',
                class_name = 'Observations::Item',
                fields = procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set_fields.RestV10CompaniesCompanyIdConfigurableFieldSetsPost_request_configurable_field_set_fields(
                    field_1 = procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set_fields_field_1.RestV10CompaniesCompanyIdConfigurableFieldSetsPost_request_configurable_field_set_fields_field_1(
                        name = 'field_1', 
                        visible = True, 
                        required = True, ), ),
                project_ids = [
                    1
                    ],
                category = 'quality',
                action_plan_type_id = 1,
                inspection_type_id = 1,
                generic_tool_id = 1,
                company_default = True,
                company_configurable_field_set_default_column_name = 'commissioning_configurable_field_set'
            )
        else:
            return RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet(
                name = 'Observation Form',
                class_name = 'Observations::Item',
                fields = procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set_fields.RestV10CompaniesCompanyIdConfigurableFieldSetsPost_request_configurable_field_set_fields(
                    field_1 = procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set_fields_field_1.RestV10CompaniesCompanyIdConfigurableFieldSetsPost_request_configurable_field_set_fields_field_1(
                        name = 'field_1', 
                        visible = True, 
                        required = True, ), ),
        )
        """

    def testRestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet(self):
        """Test RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
