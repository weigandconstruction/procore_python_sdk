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

from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest

class TestRestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest(unittest.TestCase):
    """RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest:
        """Test RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest`
        """
        model = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest()
        if include_optional:
            return RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest(
                code = '3',
                name = 'concrete',
                segment_item_list_id = 12345,
                parent_id = 56
            )
        else:
            return RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest(
                code = '3',
                name = 'concrete',
        )
        """

    def testRestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest(self):
        """Test RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
