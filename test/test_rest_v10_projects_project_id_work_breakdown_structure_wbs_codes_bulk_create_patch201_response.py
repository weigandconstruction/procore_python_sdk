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

from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_bulk_create_patch201_response import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response

class TestRestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response(unittest.TestCase):
    """RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response:
        """Test RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response`
        """
        model = RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response()
        if include_optional:
            return RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response(
                entities = [
                    procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get_200_response_inner.RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet_200_response_inner(
                        id = 1, 
                        flat_code = '01.100.Concrete.Slabs', 
                        flat_name = 'SubJob.CostCode.CostType', 
                        description = 'WBS Description', 
                        status = 'active', 
                        created_at = '2016-06-30T20:41:58Z', 
                        updated_at = '2016-08-30T18:11:43Z', 
                        segment_items = [
                            procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get_200_response_inner.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet_200_response_inner(
                                id = 456, 
                                code = '01-222', 
                                name = 'Lighting', 
                                created_at = '2016-06-30T20:41:58Z', 
                                updated_at = '2016-08-30T18:11:43Z', 
                                parent_id = 123, 
                                path_ids = [123,456], 
                                path_code = 'a', 
                                is_parent = False, 
                                path_codes = ["01 - Requirements","01-222 - Lighting"], 
                                path_names = ["01 - Requirements","01-222 - Lighting"], 
                                in_use = True, 
                                segment = {"id":3,"name":"Cost Code","type":"cost_code","position":1,"delimiter":".","required":true,"segment_items_count":2,"project_can_modify_origin_project":true,"project_can_delete_origin_company":true,"structure":"tiered","created_at":"2016-06-30T20:41:58Z","updated_at":"2016-08-30T18:11:43Z","wbs_pattern_id":4567}, 
                                status = 'active', )
                            ], 
                        wbs_pattern_id = 56, )
                    ],
                errors = [
                    None
                    ]
            )
        else:
            return RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response(
        )
        """

    def testRestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response(self):
        """Test RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
