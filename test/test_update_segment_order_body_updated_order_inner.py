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

from procore_sdk.models.update_segment_order_body_updated_order_inner import UpdateSegmentOrderBodyUpdatedOrderInner

class TestUpdateSegmentOrderBodyUpdatedOrderInner(unittest.TestCase):
    """UpdateSegmentOrderBodyUpdatedOrderInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSegmentOrderBodyUpdatedOrderInner:
        """Test UpdateSegmentOrderBodyUpdatedOrderInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSegmentOrderBodyUpdatedOrderInner`
        """
        model = UpdateSegmentOrderBodyUpdatedOrderInner()
        if include_optional:
            return UpdateSegmentOrderBodyUpdatedOrderInner(
                segment_id = 56,
                position = 1
            )
        else:
            return UpdateSegmentOrderBodyUpdatedOrderInner(
                segment_id = 56,
                position = 1,
        )
        """

    def testUpdateSegmentOrderBodyUpdatedOrderInner(self):
        """Test UpdateSegmentOrderBodyUpdatedOrderInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
