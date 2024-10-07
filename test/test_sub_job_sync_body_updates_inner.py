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

from procore_sdk.models.sub_job_sync_body_updates_inner import SubJobSyncBodyUpdatesInner

class TestSubJobSyncBodyUpdatesInner(unittest.TestCase):
    """SubJobSyncBodyUpdatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubJobSyncBodyUpdatesInner:
        """Test SubJobSyncBodyUpdatesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubJobSyncBodyUpdatesInner`
        """
        model = SubJobSyncBodyUpdatesInner()
        if include_optional:
            return SubJobSyncBodyUpdatesInner(
                id = 13513,
                name = 'Floor 2',
                code = '18',
                origin_id = '',
                origin_data = '{"data_field":{"is_important":true}}'
            )
        else:
            return SubJobSyncBodyUpdatesInner(
        )
        """

    def testSubJobSyncBodyUpdatesInner(self):
        """Test SubJobSyncBodyUpdatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
