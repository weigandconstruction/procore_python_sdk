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

from procore_sdk.models.rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response_files_inner_drawing import RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing

class TestRestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing(unittest.TestCase):
    """RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing:
        """Test RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing`
        """
        model = RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing()
        if include_optional:
            return RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing(
                dpi = 72,
                revision = '0',
                drawing_set_id = 9,
                drawing_id = 309,
                width = 4000,
                height = 3000,
                png_s3_source = 'https://storage.procore.com/us-east-1/pro-core.com/prostore/file.png?sig=deadbeafdeadbeafdeadbeafdeadbeafdeadbeafdeadbeafdeadbeafdeadbeaf',
                thumbnail_url = 'https://storage.procore.com/us-east-1/pro-core.com/prostore/thumbnail.png?sig=deadbeafdeadbeafdeadbeafdeadbeafdeadbeafdeadbeafdeadbeafdeadbeaf'
            )
        else:
            return RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing(
        )
        """

    def testRestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing(self):
        """Test RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200ResponseFilesInnerDrawing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
