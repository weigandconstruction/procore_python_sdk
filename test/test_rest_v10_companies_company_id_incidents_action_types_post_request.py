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

from procore_sdk.models.rest_v10_companies_company_id_incidents_action_types_post_request import RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest

class TestRestV10CompaniesCompanyIdIncidentsActionTypesPostRequest(unittest.TestCase):
    """RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest:
        """Test RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest`
        """
        model = RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest()
        if include_optional:
            return RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest(
                action_type = procore_sdk.models.rest_v10_companies_company_id_incidents_action_types_post_request_action_type.RestV10CompaniesCompanyIdIncidentsActionTypesPost_request_action_type(
                    name = '', 
                    active = True, )
            )
        else:
            return RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest(
                action_type = procore_sdk.models.rest_v10_companies_company_id_incidents_action_types_post_request_action_type.RestV10CompaniesCompanyIdIncidentsActionTypesPost_request_action_type(
                    name = '', 
                    active = True, ),
        )
        """

    def testRestV10CompaniesCompanyIdIncidentsActionTypesPostRequest(self):
        """Test RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
