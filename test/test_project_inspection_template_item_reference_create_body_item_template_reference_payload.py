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

from procore_sdk.models.project_inspection_template_item_reference_create_body_item_template_reference_payload import ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload

class TestProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload(unittest.TestCase):
    """ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload:
        """Test ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload`
        """
        model = ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload()
        if include_optional:
            return ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload(
                attachment = bytes(b'blah'),
                image_id = 56,
                form_id = 56,
                folder_id = 56,
                file_version_id = 56,
                drawing_revision_id = 56
            )
        else:
            return ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload(
        )
        """

    def testProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload(self):
        """Test ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
