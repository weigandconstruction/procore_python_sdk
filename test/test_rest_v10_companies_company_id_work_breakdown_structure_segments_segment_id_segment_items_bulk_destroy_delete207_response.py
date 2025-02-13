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

from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete207_response import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response

class TestRestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response(unittest.TestCase):
    """RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response:
        """Test RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response`
        """
        model = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response()
        if include_optional:
            return RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response(
                successes = [
                    123
                    ],
                failures = [
                    procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_207_response_failures_inner.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete_207_response_failures_inner(
                        id = 456, 
                        error = 'Is in use', )
                    ]
            )
        else:
            return RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response(
        )
        """

    def testRestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response(self):
        """Test RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
