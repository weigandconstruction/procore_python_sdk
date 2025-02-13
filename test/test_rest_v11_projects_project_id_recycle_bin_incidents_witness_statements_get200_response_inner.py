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

from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner

class TestRestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner(unittest.TestCase):
    """RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner:
        """Test RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner`
        """
        model = RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner()
        if include_optional:
            return RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner(
                id = 99,
                incident_id = 42,
                attachments = [
                    procore_sdk.models.incident_attachment.Incident Attachment(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        thumbnail_url = 'http://www.example.com/', 
                        name = 'january_receipt_copy.jpg', 
                        content_type = 'application/pdf', )
                    ],
                statement = '<p>I witnessed what happened.</p>',
                statement_plain_text = 'I witnessed what happened.',
                date_received = 'Tue Oct 25 00:00:00 UTC 2016',
                created_at = '2016-10-25T17:53:35Z',
                deleted_at = '2016-10-25T17:53:35Z',
                updated_at = '2016-10-25T17:53:35Z',
                witness = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_witness.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_witness(
                    id = 1, 
                    name = 'John Doe', ),
                custom_fields = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields(
                    custom_field_%{custom_field_string_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_string_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_string_definition_id_(
                        data_type = 'string', 
                        value = 'custom field value', ), 
                    custom_field_%{custom_field_decimal_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_decimal_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_decimal_definition_id_(
                        data_type = 'decimal', 
                        value = 2.2, ), 
                    custom_field_%{custom_field_boolean_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_boolean_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_boolean_definition_id_(
                        data_type = 'boolean', 
                        value = True, ), 
                    custom_field_%{custom_field_lov_entry_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id_(
                        data_type = 'lov_entry', 
                        value = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id__value.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id__value(
                            id = 1, 
                            label = 'Open', ), ), 
                    custom_field_%{custom_field_lov_entries_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_lov_entries_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_lov_entries_definition_id_(
                        data_type = 'lov_entries', ), ),
                recording = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_recording.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_recording(
                    id = 1, 
                    witness_statement_id = 8, 
                    attachment = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_recording_attachment.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_recording_attachment(
                        id = 30, 
                        content_type = 'audio/mp4', 
                        name = 'attachment.mp4', 
                        thumbnail_url = 'http://example.com/v4/d/us-east-1/attachment-thumbnail.mp4', 
                        url = 'http://example.com/v4/d/us-east-1/attachment.mp4', 
                        viewable_document_id = 4, ), 
                    captured_by = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_recording_captured_by.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_recording_captured_by(
                        id = 1, 
                        name = 'John Doe', 
                        locale = 'en-GB', 
                        login = 'test@example.com', ), 
                    created_at = '2016-10-25T17:53:35Z', )
            )
        else:
            return RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner(
        )
        """

    def testRestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner(self):
        """Test RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
