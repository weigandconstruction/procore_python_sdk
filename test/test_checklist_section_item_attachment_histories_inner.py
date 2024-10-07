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

from procore_sdk.models.checklist_section_item_attachment_histories_inner import ChecklistSectionItemAttachmentHistoriesInner

class TestChecklistSectionItemAttachmentHistoriesInner(unittest.TestCase):
    """ChecklistSectionItemAttachmentHistoriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistSectionItemAttachmentHistoriesInner:
        """Test ChecklistSectionItemAttachmentHistoriesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistSectionItemAttachmentHistoriesInner`
        """
        model = ChecklistSectionItemAttachmentHistoriesInner()
        if include_optional:
            return ChecklistSectionItemAttachmentHistoriesInner(
                id = 6485,
                created_at = '2012-10-23T21:39:40Z',
                created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                    id = 160586, 
                    login = 'exampleuser@example.com', 
                    name = 'Carl Contractor', ),
                attachment = procore_sdk.models.checklist_signature_1_attachment.Checklist_Signature_1_attachment(
                    id = 5324, 
                    url = 'http://www.example.com/', 
                    filename = 'january_receipt_copy.jpg', 
                    name = 'january_receipt_copy.jpg', )
            )
        else:
            return ChecklistSectionItemAttachmentHistoriesInner(
        )
        """

    def testChecklistSectionItemAttachmentHistoriesInner(self):
        """Test ChecklistSectionItemAttachmentHistoriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
