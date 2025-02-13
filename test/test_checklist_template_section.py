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

from procore_sdk.models.checklist_template_section import ChecklistTemplateSection

class TestChecklistTemplateSection(unittest.TestCase):
    """ChecklistTemplateSection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistTemplateSection:
        """Test ChecklistTemplateSection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistTemplateSection`
        """
        model = ChecklistTemplateSection()
        if include_optional:
            return ChecklistTemplateSection(
                id = 142,
                name = 'Fall Protection and Perimeter Protection',
                position = 2,
                items = [
                    procore_sdk.models.checklist_template_item.Checklist Template Item(
                        id = 2, 
                        name = 'Item 1', 
                        position = 1, 
                        section_id = 21, 
                        details = '+/- 1 degrees', 
                        response_set = procore_sdk.models.checklist_item_response_set.ChecklistItemResponseSet(
                            id = 1, 
                            name = 'Safety Responses', 
                            created_at = '2012-10-02T21:00Z', 
                            updated_at = '2012-10-02T21:00Z', 
                            responses = [
                                procore_sdk.models.checklist_response.Checklist Response(
                                    id = 1, 
                                    item_status_id = 1, 
                                    name = 'Safe - Knowledge', 
                                    corresponding_status = 'yes', )
                                ], ), 
                        response_type_id = 12, 
                        type = procore_sdk.models.checklist_template_item_type.Checklist_Template_Item_type(
                            id = 1, 
                            category = 'multiple choice', 
                            name = 'default', ), )
                    ],
                synced_to = procore_sdk.models.checklist_template_section_synced_to.Checklist_Template_Section_synced_to(
                    company_id = 23, 
                    list_template_id = 12, )
            )
        else:
            return ChecklistTemplateSection(
        )
        """

    def testChecklistTemplateSection(self):
        """Test ChecklistTemplateSection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
