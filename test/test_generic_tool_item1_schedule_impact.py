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

from procore_sdk.models.generic_tool_item1_schedule_impact import GenericToolItem1ScheduleImpact

class TestGenericToolItem1ScheduleImpact(unittest.TestCase):
    """GenericToolItem1ScheduleImpact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericToolItem1ScheduleImpact:
        """Test GenericToolItem1ScheduleImpact
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericToolItem1ScheduleImpact`
        """
        model = GenericToolItem1ScheduleImpact()
        if include_optional:
            return GenericToolItem1ScheduleImpact(
                status = 'yes_known',
                value = 14
            )
        else:
            return GenericToolItem1ScheduleImpact(
        )
        """

    def testGenericToolItem1ScheduleImpact(self):
        """Test GenericToolItem1ScheduleImpact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
