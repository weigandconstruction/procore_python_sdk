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

from procore_sdk.models.body126_bim_plan import Body126BimPlan

class TestBody126BimPlan(unittest.TestCase):
    """Body126BimPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body126BimPlan:
        """Test Body126BimPlan
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body126BimPlan`
        """
        model = Body126BimPlan()
        if include_optional:
            return Body126BimPlan(
                bim_level_id = 16,
                sheet_map_start = procore_sdk.models.rest_v10_bim_plans_get_200_response_inner_all_of_sheet_map_start.RestV10BimPlansGet_200_response_inner_allOf_sheet_map_start(
                    x = 6.24, 
                    y = 12.48, ),
                sheet_map_end = procore_sdk.models.rest_v10_bim_plans_get_200_response_inner_all_of_sheet_map_start.RestV10BimPlansGet_200_response_inner_allOf_sheet_map_start(
                    x = 6.24, 
                    y = 12.48, ),
                model_map_start = procore_sdk.models.rest_v10_bim_plans_get_200_response_inner_all_of_model_map_start.RestV10BimPlansGet_200_response_inner_allOf_model_map_start(
                    x = 6.24, 
                    y = 12.48, 
                    z = 24.96, ),
                model_map_end = procore_sdk.models.rest_v10_bim_plans_get_200_response_inner_all_of_model_map_start.RestV10BimPlansGet_200_response_inner_allOf_model_map_start(
                    x = 6.24, 
                    y = 12.48, 
                    z = 24.96, )
            )
        else:
            return Body126BimPlan(
                bim_level_id = 16,
        )
        """

    def testBody126BimPlan(self):
        """Test Body126BimPlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
