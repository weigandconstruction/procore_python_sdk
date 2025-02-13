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

from procore_sdk.models.timecard_entry9 import TimecardEntry9

class TestTimecardEntry9(unittest.TestCase):
    """TimecardEntry9 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimecardEntry9:
        """Test TimecardEntry9
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimecardEntry9`
        """
        model = TimecardEntry9()
        if include_optional:
            return TimecardEntry9(
                hours = '8.0',
                lunch_time = '60',
                party_id = 56,
                time_in = '2020-10-14T07:00:00Z',
                time_out = '2018-10-14T16:00:00Z',
                billable = False,
                var_date = 'Wed Oct 14 00:00:00 UTC 2020',
                datetime = '2020-05-19T12:00Z',
                description = 'This is a description.',
                timecard_time_type_id = 1,
                timesheet_id = 41823,
                cost_code_id = 12345,
                sub_job_id = 3483483,
                location_id = 161072,
                login_information_id = 2341,
                origin_id = 23423,
                origin_data = '{'example':'related data'}',
                line_item_type_id = 56
            )
        else:
            return TimecardEntry9(
                hours = '8.0',
                lunch_time = '60',
                time_in = '2020-10-14T07:00:00Z',
                time_out = '2018-10-14T16:00:00Z',
        )
        """

    def testTimecardEntry9(self):
        """Test TimecardEntry9"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
