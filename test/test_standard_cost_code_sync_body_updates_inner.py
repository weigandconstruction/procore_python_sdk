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

from procore_sdk.models.standard_cost_code_sync_body_updates_inner import StandardCostCodeSyncBodyUpdatesInner

class TestStandardCostCodeSyncBodyUpdatesInner(unittest.TestCase):
    """StandardCostCodeSyncBodyUpdatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StandardCostCodeSyncBodyUpdatesInner:
        """Test StandardCostCodeSyncBodyUpdatesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StandardCostCodeSyncBodyUpdatesInner`
        """
        model = StandardCostCodeSyncBodyUpdatesInner()
        if include_optional:
            return StandardCostCodeSyncBodyUpdatesInner(
                name = 'General Requirements',
                id = 123,
                code = '2-075',
                parent_id = 456,
                origin_id = 'OID-123',
                origin_data = 'OD-234'
            )
        else:
            return StandardCostCodeSyncBodyUpdatesInner(
        )
        """

    def testStandardCostCodeSyncBodyUpdatesInner(self):
        """Test StandardCostCodeSyncBodyUpdatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
