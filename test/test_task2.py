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

from procore_sdk.models.task2 import Task2

class TestTask2(unittest.TestCase):
    """Task2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Task2:
        """Test Task2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Task2`
        """
        model = Task2()
        if include_optional:
            return Task2(
                id = 1359235,
                name = 'INTERIOR',
                key = '101429|40e65ab5-07a5-4cb3-88c0-bc691c3902e0'
            )
        else:
            return Task2(
        )
        """

    def testTask2(self):
        """Test Task2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
