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

from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete_request_time_and_material_entry_attachment import RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment

class TestRestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment(unittest.TestCase):
    """RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment:
        """Test RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment`
        """
        model = RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment()
        if include_optional:
            return RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment(
                time_and_material_entry_attachment_ids = [
                    65
                    ]
            )
        else:
            return RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment(
        )
        """

    def testRestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment(self):
        """Test RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequestTimeAndMaterialEntryAttachment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
