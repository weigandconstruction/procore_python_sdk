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

from procore_sdk.models.body130_bim_model_revision import Body130BimModelRevision

class TestBody130BimModelRevision(unittest.TestCase):
    """Body130BimModelRevision unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body130BimModelRevision:
        """Test Body130BimModelRevision
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body130BimModelRevision`
        """
        model = Body130BimModelRevision()
        if include_optional:
            return Body130BimModelRevision(
                bim_file_id = 123,
                bim_model_id = 456,
                home_viewpoint_id = 346,
                suitability = 'issued_for_coordination',
                publisher_name = 'nw_publisher',
                publisher_version = '3.1.6',
                min_boundary = procore_sdk.models.rest_v10_bim_models_get_200_response_inner_one_of_1_current_revision_min_boundary.RestV10BimModelsGet_200_response_inner_oneOf_1_current_revision_min_boundary(
                    x = '6.24', 
                    y = '12.48', 
                    z = '24.96', ),
                max_boundary = procore_sdk.models.rest_v10_bim_models_get_200_response_inner_one_of_1_current_revision_min_boundary.RestV10BimModelsGet_200_response_inner_oneOf_1_current_revision_min_boundary(
                    x = '6.24', 
                    y = '12.48', 
                    z = '24.96', ),
                rotation = procore_sdk.models.rest_v10_bim_models_get_200_response_inner_one_of_1_current_revision_min_boundary.RestV10BimModelsGet_200_response_inner_oneOf_1_current_revision_min_boundary(
                    x = '6.24', 
                    y = '12.48', 
                    z = '24.96', ),
                geometry_file_bundle_id = 148,
                published_model_upload_uuid = '1R9QSTJ4ZHYYJ2T6TPQBGNSEH8',
                object_definition_upload_uuid = '1Z0REJ4ZHYYJ2T6TPQBGNSEH81',
                geometry_file_id = 4766,
                property_file_id = 4862
            )
        else:
            return Body130BimModelRevision(
                bim_file_id = 123,
                bim_model_id = 456,
                suitability = 'issued_for_coordination',
                min_boundary = procore_sdk.models.rest_v10_bim_models_get_200_response_inner_one_of_1_current_revision_min_boundary.RestV10BimModelsGet_200_response_inner_oneOf_1_current_revision_min_boundary(
                    x = '6.24', 
                    y = '12.48', 
                    z = '24.96', ),
                max_boundary = procore_sdk.models.rest_v10_bim_models_get_200_response_inner_one_of_1_current_revision_min_boundary.RestV10BimModelsGet_200_response_inner_oneOf_1_current_revision_min_boundary(
                    x = '6.24', 
                    y = '12.48', 
                    z = '24.96', ),
        )
        """

    def testBody130BimModelRevision(self):
        """Test Body130BimModelRevision"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
