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

from procore_sdk.models.rest_v10_companies_company_id_invoices_async_jobs_uuid_get200_response_result import RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult

class TestRestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult(unittest.TestCase):
    """RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult:
        """Test RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult`
        """
        model = RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult()
        if include_optional:
            return RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult(
                url = 'https://example.com/payment_application_1.pdf'
            )
        else:
            return RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult(
        )
        """

    def testRestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult(self):
        """Test RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200ResponseResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
