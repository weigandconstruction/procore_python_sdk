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

from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post201_response import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response

class TestRestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response(unittest.TestCase):
    """RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response:
        """Test RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response`
        """
        model = RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response()
        if include_optional:
            return RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response(
                data = procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get_200_response_data_inner.RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet_200_response_data_inner(
                    id = '21', 
                    requested_by_id = '44', 
                    signatory = null, 
                    signature = procore_sdk.models.checklist_signature.Checklist Signature(
                        id = '5324', 
                        captured_by = null, 
                        captured_at = '2012-10-23T21:39:40Z', 
                        attachment = procore_sdk.models.inspection_item_signature_attachment.Inspection_Item_Signature_attachment(
                            id = '5324', 
                            url = 'http://www.example.com/', 
                            filename = 'january_receipt_copy.jpg', 
                            name = 'january_receipt_copy.jpg', ), ), )
            )
        else:
            return RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response(
        )
        """

    def testRestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response(self):
        """Test RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
