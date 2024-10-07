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

from procore_sdk.models.rest_v10_companies_company_id_concierge_patch_request import RestV10CompaniesCompanyIdConciergePatchRequest

class TestRestV10CompaniesCompanyIdConciergePatchRequest(unittest.TestCase):
    """RestV10CompaniesCompanyIdConciergePatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdConciergePatchRequest:
        """Test RestV10CompaniesCompanyIdConciergePatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdConciergePatchRequest`
        """
        model = RestV10CompaniesCompanyIdConciergePatchRequest()
        if include_optional:
            return RestV10CompaniesCompanyIdConciergePatchRequest(
                concierge = procore_sdk.models.rest_v10_companies_company_id_concierge_patch_request_concierge.RestV10CompaniesCompanyIdConciergePatch_request_concierge(
                    estimated_initial_projects = 3, 
                    estimated_initial_users = 15, )
            )
        else:
            return RestV10CompaniesCompanyIdConciergePatchRequest(
        )
        """

    def testRestV10CompaniesCompanyIdConciergePatchRequest(self):
        """Test RestV10CompaniesCompanyIdConciergePatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
