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

from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner

class TestRestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner:
        """Test RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner(
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
                wbs_pattern_id = 56
            )
        else:
            return RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
