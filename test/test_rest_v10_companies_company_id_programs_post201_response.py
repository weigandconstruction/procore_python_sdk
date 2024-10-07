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

from procore_sdk.models.rest_v10_companies_company_id_programs_post201_response import RestV10CompaniesCompanyIdProgramsPost201Response

class TestRestV10CompaniesCompanyIdProgramsPost201Response(unittest.TestCase):
    """RestV10CompaniesCompanyIdProgramsPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdProgramsPost201Response:
        """Test RestV10CompaniesCompanyIdProgramsPost201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdProgramsPost201Response`
        """
        model = RestV10CompaniesCompanyIdProgramsPost201Response()
        if include_optional:
            return RestV10CompaniesCompanyIdProgramsPost201Response(
                id = 1,
                name = 'NW USA',
                address_freeform = 'Seattle',
                website = 'http://www.example.com',
                zip = '91013',
                longitude = '1',
                latitude = '1',
                projects = [
                    procore_sdk.models.rest_v10_companies_company_id_programs_post_201_response_all_of_projects_inner.RestV10CompaniesCompanyIdProgramsPost_201_response_allOf_projects_inner(
                        id = 46146, 
                        name = '2014 Draft', 
                        project_number = '1234', )
                    ]
            )
        else:
            return RestV10CompaniesCompanyIdProgramsPost201Response(
        )
        """

    def testRestV10CompaniesCompanyIdProgramsPost201Response(self):
        """Test RestV10CompaniesCompanyIdProgramsPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
