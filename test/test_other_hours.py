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

from procore_sdk.models.other_hours import OtherHours

class TestOtherHours(unittest.TestCase):
    """OtherHours unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OtherHours:
        """Test OtherHours
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OtherHours`
        """
        model = OtherHours()
        if include_optional:
            return OtherHours(
                hours = 40,
                project = procore_sdk.models.other_hours_project.Other_Hours_project(
                    id = 1, 
                    name = 'Hotel Remodel', )
            )
        else:
            return OtherHours(
        )
        """

    def testOtherHours(self):
        """Test OtherHours"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
