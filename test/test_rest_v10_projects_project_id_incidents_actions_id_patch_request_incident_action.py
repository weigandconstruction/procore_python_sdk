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

from procore_sdk.models.rest_v10_projects_project_id_incidents_actions_id_patch_request_incident_action import RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction

class TestRestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction(unittest.TestCase):
    """RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction:
        """Test RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction`
        """
        model = RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction()
        if include_optional:
            return RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction(
                incident_id = 56,
                action_type_id = 56,
                description = '<p>I took action.</p>',
                drawing_revision_ids = [4,5],
                file_version_ids = [6,7],
                form_ids = [7,8],
                image_ids = [9,10],
                upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"],
                custom_field_custom_field_definition_id = custom field value
            )
        else:
            return RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction(
        )
        """

    def testRestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction(self):
        """Test RestV10ProjectsProjectIdIncidentsActionsIdPatchRequestIncidentAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
