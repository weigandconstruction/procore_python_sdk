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

from procore_sdk.models.item_response_set1 import ItemResponseSet1

class TestItemResponseSet1(unittest.TestCase):
    """ItemResponseSet1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemResponseSet1:
        """Test ItemResponseSet1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemResponseSet1`
        """
        model = ItemResponseSet1()
        if include_optional:
            return ItemResponseSet1(
                name = 'Modified Safety Responses',
                active = True
            )
        else:
            return ItemResponseSet1(
        )
        """

    def testItemResponseSet1(self):
        """Test ItemResponseSet1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
