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

from procore_sdk.models.upload_uuid import UploadUuid

class TestUploadUuid(unittest.TestCase):
    """UploadUuid unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadUuid:
        """Test UploadUuid
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadUuid`
        """
        model = UploadUuid()
        if include_optional:
            return UploadUuid(
                name = 'my.pdf',
                notes = 'This file version is good',
                upload_uuid = '1QJ83Q56CVQR4X3C0JG7YV86F8'
            )
        else:
            return UploadUuid(
                upload_uuid = '1QJ83Q56CVQR4X3C0JG7YV86F8',
        )
        """

    def testUploadUuid(self):
        """Test UploadUuid"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
