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

from procore_sdk.models.timecard_time_type2 import TimecardTimeType2

class TestTimecardTimeType2(unittest.TestCase):
    """TimecardTimeType2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimecardTimeType2:
        """Test TimecardTimeType2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimecardTimeType2`
        """
        model = TimecardTimeType2()
        if include_optional:
            return TimecardTimeType2(
                id = 1,
                time_type = 'Another Time',
                abbreviated_time_type = 'true',
                var_global = False
            )
        else:
            return TimecardTimeType2(
        )
        """

    def testTimecardTimeType2(self):
        """Test TimecardTimeType2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
