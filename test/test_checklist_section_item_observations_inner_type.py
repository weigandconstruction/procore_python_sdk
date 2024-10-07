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

from procore_sdk.models.checklist_section_item_observations_inner_type import ChecklistSectionItemObservationsInnerType

class TestChecklistSectionItemObservationsInnerType(unittest.TestCase):
    """ChecklistSectionItemObservationsInnerType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistSectionItemObservationsInnerType:
        """Test ChecklistSectionItemObservationsInnerType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistSectionItemObservationsInnerType`
        """
        model = ChecklistSectionItemObservationsInnerType()
        if include_optional:
            return ChecklistSectionItemObservationsInnerType(
                id = 4952,
                name = 'Deficiency',
                active = True
            )
        else:
            return ChecklistSectionItemObservationsInnerType(
        )
        """

    def testChecklistSectionItemObservationsInnerType(self):
        """Test ChecklistSectionItemObservationsInnerType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
