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

from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get401_response import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response

class TestRestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response(unittest.TestCase):
    """RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response:
        """Test RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response`
        """
        model = RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response()
        if include_optional:
            return RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response(
                code = 56,
                message = '',
                fields = '',
                reason = '',
                error = 'Invalid Token'
            )
        else:
            return RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response(
        )
        """

    def testRestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response(self):
        """Test RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
