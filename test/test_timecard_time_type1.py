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

from procore_sdk.models.timecard_time_type1 import TimecardTimeType1

class TestTimecardTimeType1(unittest.TestCase):
    """TimecardTimeType1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimecardTimeType1:
        """Test TimecardTimeType1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimecardTimeType1`
        """
        model = TimecardTimeType1()
        if include_optional:
            return TimecardTimeType1(
                id = 1,
                time_type = 'Another Time',
                abbreviated_time_type = 'REG',
                var_global = False
            )
        else:
            return TimecardTimeType1(
        )
        """

    def testTimecardTimeType1(self):
        """Test TimecardTimeType1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
