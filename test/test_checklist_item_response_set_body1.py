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

from procore_sdk.models.checklist_item_response_set_body1 import ChecklistItemResponseSetBody1

class TestChecklistItemResponseSetBody1(unittest.TestCase):
    """ChecklistItemResponseSetBody1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistItemResponseSetBody1:
        """Test ChecklistItemResponseSetBody1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistItemResponseSetBody1`
        """
        model = ChecklistItemResponseSetBody1()
        if include_optional:
            return ChecklistItemResponseSetBody1(
                response_set = procore_sdk.models.item_response_set.Item Response Set(
                    name = 'Modified Safety Responses', 
                    active = True, )
            )
        else:
            return ChecklistItemResponseSetBody1(
                response_set = procore_sdk.models.item_response_set.Item Response Set(
                    name = 'Modified Safety Responses', 
                    active = True, ),
        )
        """

    def testChecklistItemResponseSetBody1(self):
        """Test ChecklistItemResponseSetBody1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
