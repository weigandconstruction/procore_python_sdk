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

from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest

class TestRestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest(unittest.TestCase):
    """RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest:
        """Test RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest`
        """
        model = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest()
        if include_optional:
            return RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest(
                ids = [23,24],
                attributes = procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request_attributes.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatch_request_attributes(
                    status = 'inactive', )
            )
        else:
            return RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest(
                ids = [23,24],
                attributes = procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request_attributes.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatch_request_attributes(
                    status = 'inactive', ),
        )
        """

    def testRestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest(self):
        """Test RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
