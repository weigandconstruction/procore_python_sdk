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

from procore_sdk.models.rest_v10_projects_project_id_inspection_templates_inspection_template_id_item_references_get200_response_inner_payload_attachment import RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment

class TestRestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment(unittest.TestCase):
    """RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment:
        """Test RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment`
        """
        model = RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment()
        if include_optional:
            return RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment(
                id = 5324,
                url = 'http://www.example.com/',
                thumbnail_url = 'http://www.example.com/',
                name = 'january_receipt_copy.jpg',
                content_type = 'image/jpg'
            )
        else:
            return RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment(
        )
        """

    def testRestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment(self):
        """Test RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
