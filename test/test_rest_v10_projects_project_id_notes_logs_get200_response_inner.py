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

from procore_sdk.models.rest_v10_projects_project_id_notes_logs_get200_response_inner import RestV10ProjectsProjectIdNotesLogsGet200ResponseInner

class TestRestV10ProjectsProjectIdNotesLogsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdNotesLogsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdNotesLogsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdNotesLogsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdNotesLogsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdNotesLogsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdNotesLogsGet200ResponseInner(
                id = 333675,
                comment = 'Notes Log comment',
                created_at = '2012-10-23T21:39:40Z',
                var_date = 'Thu May 19 00:00:00 UTC 2016',
                datetime = '2016-05-19T12:00Z',
                daily_log_header_id = 151335,
                deleted_at = '2017-07-29T21:39:40Z',
                is_issue_day = False,
                permissions = procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get_200_response_inner_permissions.RestV10ProjectsProjectIdVisitorLogsGet_200_response_inner_permissions(
                    can_update = True, 
                    can_delete = False, ),
                position = 11241,
                status = 'pending',
                updated_at = '2012-10-24T21:39:40Z',
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                created_by_collaborator = True,
                custom_fields = procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get_200_response_inner_custom_fields.RestV10ProjectsProjectIdVisitorLogsGet_200_response_inner_custom_fields(
                    custom_field_%{custom_field_string_definition_id} = procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get_200_response_inner_custom_fields_custom_field___custom_field_string_definition_id_.RestV10ProjectsProjectIdVisitorLogsGet_200_response_inner_custom_fields_custom_field___custom_field_string_definition_id_(
                        data_type = 'string', 
                        value = 'custom field value', ), 
                    custom_field_%{custom_field_decimal_definition_id} = procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get_200_response_inner_custom_fields_custom_field___custom_field_decimal_definition_id_.RestV10ProjectsProjectIdVisitorLogsGet_200_response_inner_custom_fields_custom_field___custom_field_decimal_definition_id_(
                        data_type = 'decimal', 
                        value = 2.2, ), 
                    custom_field_%{custom_field_boolean_definition_id} = procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get_200_response_inner_custom_fields_custom_field___custom_field_boolean_definition_id_.RestV10ProjectsProjectIdVisitorLogsGet_200_response_inner_custom_fields_custom_field___custom_field_boolean_definition_id_(
                        data_type = 'boolean', 
                        value = True, ), 
                    custom_field_%{custom_field_lov_entry_definition_id} = procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id_.RestV10ProjectsProjectIdVisitorLogsGet_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id_(
                        data_type = 'lov_entry', 
                        value = procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id__value.RestV10ProjectsProjectIdVisitorLogsGet_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id__value(
                            id = 1, 
                            label = 'Open', ), ), 
                    custom_field_%{custom_field_lov_entries_definition_id} = procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get_200_response_inner_custom_fields_custom_field___custom_field_lov_entries_definition_id_.RestV10ProjectsProjectIdVisitorLogsGet_200_response_inner_custom_fields_custom_field___custom_field_lov_entries_definition_id_(
                        data_type = 'lov_entries', ), ),
                location = procore_sdk.models.location.Location(
                    id = 15504, 
                    name = 'North Building>First Floor>Electrical Closet', 
                    node_name = 'Electrical Closet', 
                    parent_id = 788866, 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', ),
                attachments = [
                    procore_sdk.models.rest_v10_projects_project_id_notes_logs_get_200_response_inner_attachments_inner.RestV10ProjectsProjectIdNotesLogsGet_200_response_inner_attachments_inner(
                        id = 56, 
                        content_type = 'image/jpeg', 
                        name = '', 
                        url = '', 
                        filename = '', 
                        share_url = 'https://example.com/utilities/prostore_local/62d97223fd22a7806c3c7b12fc5ba9ee900d?company_id=15', 
                        viewable_type = 'image', 
                        viewable_url = 'https://example.com/15/project/daily_log/viewable_document_image_show?holder_class=AccidentLog\u0026holder_id=13\u0026prostore_file_id=76094', )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdNotesLogsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdNotesLogsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdNotesLogsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
