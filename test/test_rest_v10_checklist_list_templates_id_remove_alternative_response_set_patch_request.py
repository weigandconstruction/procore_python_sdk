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

from procore_sdk.models.rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch_request import RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest

class TestRestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest(unittest.TestCase):
    """RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest:
        """Test RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest`
        """
        model = RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest()
        if include_optional:
            return RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest(
                project_id = 56
            )
        else:
            return RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest(
                project_id = 56,
        )
        """

    def testRestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest(self):
        """Test RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
