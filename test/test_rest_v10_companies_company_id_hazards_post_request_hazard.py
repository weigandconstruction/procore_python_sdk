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

from procore_sdk.models.rest_v10_companies_company_id_hazards_post_request_hazard import RestV10CompaniesCompanyIdHazardsPostRequestHazard

class TestRestV10CompaniesCompanyIdHazardsPostRequestHazard(unittest.TestCase):
    """RestV10CompaniesCompanyIdHazardsPostRequestHazard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdHazardsPostRequestHazard:
        """Test RestV10CompaniesCompanyIdHazardsPostRequestHazard
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdHazardsPostRequestHazard`
        """
        model = RestV10CompaniesCompanyIdHazardsPostRequestHazard()
        if include_optional:
            return RestV10CompaniesCompanyIdHazardsPostRequestHazard(
                name = '',
                active = True
            )
        else:
            return RestV10CompaniesCompanyIdHazardsPostRequestHazard(
                name = '',
        )
        """

    def testRestV10CompaniesCompanyIdHazardsPostRequestHazard(self):
        """Test RestV10CompaniesCompanyIdHazardsPostRequestHazard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
