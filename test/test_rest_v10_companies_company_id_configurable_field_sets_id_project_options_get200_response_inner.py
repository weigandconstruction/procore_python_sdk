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

from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_project_options_get200_response_inner import RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner

class TestRestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner(unittest.TestCase):
    """RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner:
        """Test RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner`
        """
        model = RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner()
        if include_optional:
            return RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner(
                id = 99,
                name = 'More Mesa Renovation',
                assigned = True,
                configurable_field_set_name = 'Observation Fields'
            )
        else:
            return RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner(
        )
        """

    def testRestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner(self):
        """Test RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
