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

from procore_sdk.models.checklist_section_item1_observations_inner_type import ChecklistSectionItem1ObservationsInnerType

class TestChecklistSectionItem1ObservationsInnerType(unittest.TestCase):
    """ChecklistSectionItem1ObservationsInnerType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistSectionItem1ObservationsInnerType:
        """Test ChecklistSectionItem1ObservationsInnerType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistSectionItem1ObservationsInnerType`
        """
        model = ChecklistSectionItem1ObservationsInnerType()
        if include_optional:
            return ChecklistSectionItem1ObservationsInnerType(
                id = 4952,
                name = 'Deficiency'
            )
        else:
            return ChecklistSectionItem1ObservationsInnerType(
        )
        """

    def testChecklistSectionItem1ObservationsInnerType(self):
        """Test ChecklistSectionItem1ObservationsInnerType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
