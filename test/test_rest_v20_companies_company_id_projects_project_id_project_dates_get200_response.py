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

from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_project_dates_get200_response import RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response

class TestRestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response(unittest.TestCase):
    """RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response:
        """Test RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response`
        """
        model = RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response()
        if include_optional:
            return RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response(
                data = [
                    {"id":1,"name":"Start","date":"2014-07-09"}
                    ]
            )
        else:
            return RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response(
        )
        """

    def testRestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response(self):
        """Test RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
