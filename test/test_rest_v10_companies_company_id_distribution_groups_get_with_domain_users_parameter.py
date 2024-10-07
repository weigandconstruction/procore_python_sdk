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

from procore_sdk.models.rest_v10_companies_company_id_distribution_groups_get_with_domain_users_parameter import RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter

class TestRestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter(unittest.TestCase):
    """RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter:
        """Test RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter`
        """
        model = RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter()
        if include_optional:
            return RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter(
                domain_id = 12,
                provider_id = 199432
            )
        else:
            return RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter(
        )
        """

    def testRestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter(self):
        """Test RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
