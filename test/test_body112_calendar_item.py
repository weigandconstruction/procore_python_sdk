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

from procore_sdk.models.body112_calendar_item import Body112CalendarItem

class TestBody112CalendarItem(unittest.TestCase):
    """Body112CalendarItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body112CalendarItem:
        """Test Body112CalendarItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body112CalendarItem`
        """
        model = Body112CalendarItem()
        if include_optional:
            return Body112CalendarItem(
                assigned_id = 56,
                color = '#A4505D',
                description = 'Use some power tools to fix the drywall.',
                finish = 'Sun Feb 02 00:00:00 UTC 2020',
                name = 'Fix Drywall',
                percentage = 50,
                private = False,
                start = 'Wed Jan 01 00:00:00 UTC 2020'
            )
        else:
            return Body112CalendarItem(
        )
        """

    def testBody112CalendarItem(self):
        """Test Body112CalendarItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
