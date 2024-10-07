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

from procore_sdk.models.line_item_type_sync_body_updates_inner import LineItemTypeSyncBodyUpdatesInner

class TestLineItemTypeSyncBodyUpdatesInner(unittest.TestCase):
    """LineItemTypeSyncBodyUpdatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LineItemTypeSyncBodyUpdatesInner:
        """Test LineItemTypeSyncBodyUpdatesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LineItemTypeSyncBodyUpdatesInner`
        """
        model = LineItemTypeSyncBodyUpdatesInner()
        if include_optional:
            return LineItemTypeSyncBodyUpdatesInner(
                id = 12345,
                name = 'Equipment',
                csv_import_code = 'LB',
                base_type = 'materials',
                origin_data = 'OD-2398273424',
                origin_id = 'ABC123'
            )
        else:
            return LineItemTypeSyncBodyUpdatesInner(
        )
        """

    def testLineItemTypeSyncBodyUpdatesInner(self):
        """Test LineItemTypeSyncBodyUpdatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
