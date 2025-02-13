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

from procore_sdk.models.segmented_upload_segments_inner import SegmentedUploadSegmentsInner

class TestSegmentedUploadSegmentsInner(unittest.TestCase):
    """SegmentedUploadSegmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SegmentedUploadSegmentsInner:
        """Test SegmentedUploadSegmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SegmentedUploadSegmentsInner`
        """
        model = SegmentedUploadSegmentsInner()
        if include_optional:
            return SegmentedUploadSegmentsInner(
                etag = '9c6243014e7ae154a58d29294906d4a960c60765',
                sha256 = '70c50ce1892d79bc900a0e753b12126273ea8e80051386531b3c10dc68d33926',
                size = 5242880,
                url = 'https://procore-uploads.s3.amazonaws.com',
                headers = procore_sdk.models.segmented_upload_segments_inner_headers.segmented_upload_segments_inner_headers(
                    x_amz_content_sha256 = '70c50ce1892d79bc900a0e753b12126273ea8e80051386531b3c10dc68d33926', 
                    content_length = '5242880', )
            )
        else:
            return SegmentedUploadSegmentsInner(
        )
        """

    def testSegmentedUploadSegmentsInner(self):
        """Test SegmentedUploadSegmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
