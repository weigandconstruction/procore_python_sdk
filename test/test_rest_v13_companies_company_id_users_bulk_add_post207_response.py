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

from procore_sdk.models.rest_v13_companies_company_id_users_bulk_add_post207_response import RestV13CompaniesCompanyIdUsersBulkAddPost207Response

class TestRestV13CompaniesCompanyIdUsersBulkAddPost207Response(unittest.TestCase):
    """RestV13CompaniesCompanyIdUsersBulkAddPost207Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV13CompaniesCompanyIdUsersBulkAddPost207Response:
        """Test RestV13CompaniesCompanyIdUsersBulkAddPost207Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV13CompaniesCompanyIdUsersBulkAddPost207Response`
        """
        model = RestV13CompaniesCompanyIdUsersBulkAddPost207Response()
        if include_optional:
            return RestV13CompaniesCompanyIdUsersBulkAddPost207Response(
                entities = [
                    { }
                    ],
                errors = [
                    { }
                    ]
            )
        else:
            return RestV13CompaniesCompanyIdUsersBulkAddPost207Response(
        )
        """

    def testRestV13CompaniesCompanyIdUsersBulkAddPost207Response(self):
        """Test RestV13CompaniesCompanyIdUsersBulkAddPost207Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
