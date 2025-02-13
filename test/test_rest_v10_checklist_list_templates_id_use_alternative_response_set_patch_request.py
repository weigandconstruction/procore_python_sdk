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

from procore_sdk.models.rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request import RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest

class TestRestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest(unittest.TestCase):
    """RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest:
        """Test RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest`
        """
        model = RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest()
        if include_optional:
            return RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest(
                project_id = 56,
                alternative_response_set_id = 1
            )
        else:
            return RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest(
                project_id = 56,
                alternative_response_set_id = 1,
        )
        """

    def testRestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest(self):
        """Test RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
