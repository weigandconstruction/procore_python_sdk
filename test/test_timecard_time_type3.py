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

from procore_sdk.models.timecard_time_type3 import TimecardTimeType3

class TestTimecardTimeType3(unittest.TestCase):
    """TimecardTimeType3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimecardTimeType3:
        """Test TimecardTimeType3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimecardTimeType3`
        """
        model = TimecardTimeType3()
        if include_optional:
            return TimecardTimeType3(
                id = 1,
                abbreviated_time_type = 'true',
                company_id = 15125,
                var_global = False,
                time_type = 'Another Time'
            )
        else:
            return TimecardTimeType3(
        )
        """

    def testTimecardTimeType3(self):
        """Test TimecardTimeType3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
