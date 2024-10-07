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

from procore_sdk.models.checklist import Checklist

class TestChecklist(unittest.TestCase):
    """Checklist unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Checklist:
        """Test Checklist
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Checklist`
        """
        model = Checklist()
        if include_optional:
            return Checklist(
                id = 42,
                name = 'Window Inspection',
                list_template_id = 1,
                list_template_name = 'Window Inspection v2',
                number = 1,
                status = 'Closed',
                location = procore_sdk.models.location.Location(
                    id = 15504, 
                    name = '1space>1 space', 
                    code = 'code', 
                    node_name = '1 space', 
                    parent_id = 788866, 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', ),
                created_at = '2017-10-31T23:36:30Z',
                updated_at = '2018-12-11T04:58:42Z',
                closed_at = '2018-12-11T04:58:42Z',
                drawing_ids = [
                    56
                    ],
                current_drawing_revision_ids = [
                    56
                    ],
                description = 'Checklist for circular windows',
                deleted = False,
                due_at = '2019-08-18T23:36:30Z',
                identifier = '176-09B',
                inspection_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                inspection_type = procore_sdk.models.inspection_type.Inspection Type(
                    id = 142, 
                    name = 'Safety Compliance', 
                    created_at = '2014-12-10T23:36:30Z', 
                    updated_at = '2014-12-11T04:58:42Z', ),
                private = False,
                created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                    id = 160586, 
                    login = 'exampleuser@example.com', 
                    name = 'Carl Contractor', ),
                closed_by = procore_sdk.models.checklist_closed_by.Checklist_closed_by(
                    id = 160586, 
                    login = 'exampleuser@example.com', 
                    name = 'Carl Contractor', ),
                responsible_contractor = procore_sdk.models.checklist_responsible_contractor.Checklist_responsible_contractor(
                    id = 1, 
                    name = 'Freddie's Excavating', ),
                point_of_contact = procore_sdk.models.checklist_closed_by.Checklist_closed_by(
                    id = 160586, 
                    login = 'exampleuser@example.com', 
                    name = 'Carl Contractor', ),
                trade = procore_sdk.models.trade.Trade(
                    id = 999, 
                    name = '09 - acoustical panels', 
                    active = True, 
                    updated_at = '2016-08-01T23:33:54Z', ),
                inspectors = [
                    procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                        id = 160586, 
                        login = 'exampleuser@example.com', 
                        name = 'Carl Contractor', )
                    ],
                distribution_members = [
                    procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                        id = 160586, 
                        login = 'exampleuser@example.com', 
                        name = 'Carl Contractor', )
                    ],
                signature_requests = [
                    procore_sdk.models.checklist_signature_request.Checklist Signature Request(
                        id = 21, 
                        signatory = null, 
                        signature = procore_sdk.models.checklist_signature.Checklist Signature(
                            id = 5324, 
                            captured_by = null, 
                            captured_at = '2012-10-23T21:39:40Z', 
                            attachment = procore_sdk.models.checklist_signature_1_attachment.Checklist_Signature_1_attachment(
                                id = 5324, 
                                url = 'http://www.example.com/', 
                                filename = 'january_receipt_copy.jpg', 
                                name = 'january_receipt_copy.jpg', ), ), )
                    ],
                managed_equipment_id = 1,
                specification_section = procore_sdk.models.checklist_specification_section.Checklist_specification_section(
                    id = 1, 
                    current_revision_id = 11, 
                    description = 'Vinyl Windows', 
                    section = '08560', 
                    latest_revision_url = 'link_to_pdf', ),
                attachments = [
                    procore_sdk.models.checklist_(inspection)_attachment.Checklist (Inspection) Attachment(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        thumbnail_url = 'http://www.example.com/', 
                        name = 'january_receipt_copy.jpg', 
                        filename = 'january_receipt_copy.jpg', 
                        content_type = 'application/pdf', 
                        viewable_document_id = 492, )
                    ],
                conforming_item_count = 1,
                deficient_item_count = 1,
                not_applicable_item_count = 0,
                neutral_item_count = 1,
                inspected_item_count = 4,
                observations_count = 2,
                closed_observations_count = 1,
                item_count = 1,
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
                template_id = 176,
                overdue = True
            )
        else:
            return Checklist(
        )
        """

    def testChecklist(self):
        """Test Checklist"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
