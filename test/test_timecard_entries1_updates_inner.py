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

from procore_sdk.models.timecard_entries1_updates_inner import TimecardEntries1UpdatesInner

class TestTimecardEntries1UpdatesInner(unittest.TestCase):
    """TimecardEntries1UpdatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimecardEntries1UpdatesInner:
        """Test TimecardEntries1UpdatesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimecardEntries1UpdatesInner`
        """
        model = TimecardEntries1UpdatesInner()
        if include_optional:
            return TimecardEntries1UpdatesInner(
                id = 1011121314
            )
        else:
            return TimecardEntries1UpdatesInner(
        )
        """

    def testTimecardEntries1UpdatesInner(self):
        """Test TimecardEntries1UpdatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
