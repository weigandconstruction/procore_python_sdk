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

from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest

class TestRestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest(unittest.TestCase):
    """RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest:
        """Test RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest`
        """
        model = RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest()
        if include_optional:
            return RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest(
                signatory_id = '44'
            )
        else:
            return RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest(
        )
        """

    def testRestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest(self):
        """Test RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
