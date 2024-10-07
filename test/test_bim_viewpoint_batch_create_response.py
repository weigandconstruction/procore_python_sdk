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

from procore_sdk.models.bim_viewpoint_batch_create_response import BIMViewpointBatchCreateResponse

class TestBIMViewpointBatchCreateResponse(unittest.TestCase):
    """BIMViewpointBatchCreateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BIMViewpointBatchCreateResponse:
        """Test BIMViewpointBatchCreateResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BIMViewpointBatchCreateResponse`
        """
        model = BIMViewpointBatchCreateResponse()
        if include_optional:
            return BIMViewpointBatchCreateResponse(
                bim_viewpoints = [
                    procore_sdk.models.rest_v10_coordination_issues_get_200_response_inner_all_of_viewpoints_inner.RestV10CoordinationIssuesGet_200_response_inner_allOf_viewpoints_inner()
                    ],
                errors = [
                    procore_sdk.models.bim_viewpoint_batch_create_response_errors_inner.BIM_Viewpoint_Batch_create_response_errors_inner()
                    ]
            )
        else:
            return BIMViewpointBatchCreateResponse(
        )
        """

    def testBIMViewpointBatchCreateResponse(self):
        """Test BIMViewpointBatchCreateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
