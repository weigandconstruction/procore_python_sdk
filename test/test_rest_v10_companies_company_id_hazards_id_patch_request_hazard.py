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

from procore_sdk.models.rest_v10_companies_company_id_hazards_id_patch_request_hazard import RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard

class TestRestV10CompaniesCompanyIdHazardsIdPatchRequestHazard(unittest.TestCase):
    """RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard:
        """Test RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard`
        """
        model = RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard()
        if include_optional:
            return RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard(
                name = '',
                active = True
            )
        else:
            return RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard(
        )
        """

    def testRestV10CompaniesCompanyIdHazardsIdPatchRequestHazard(self):
        """Test RestV10CompaniesCompanyIdHazardsIdPatchRequestHazard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
