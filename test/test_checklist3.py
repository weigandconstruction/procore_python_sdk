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

from procore_sdk.models.checklist3 import Checklist3

class TestChecklist3(unittest.TestCase):
    """Checklist3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Checklist3:
        """Test Checklist3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Checklist3`
        """
        model = Checklist3()
        if include_optional:
            return Checklist3(
                id = 1445,
                inspection_type = procore_sdk.models.inspection_type.Inspection Type(
                    id = 142, 
                    name = 'Safety Compliance', 
                    created_at = '2014-12-10T23:36:30Z', 
                    updated_at = '2014-12-11T04:58:42Z', ),
                list_template_id = 1,
                name = 'Framing List',
                description = 'Checking the framing',
                distribution_members = [
                    procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                        id = 160586, 
                        login = 'exampleuser@example.com', 
                        name = 'Carl Contractor', )
                    ],
                due_at = '2019-08-18T23:36:30Z',
                identifier = '176-09B',
                number = 1,
                status = 'Closed',
                inspection_date = 'Thu Nov 06 00:00:00 UTC 2014',
                created_at = '2014-11-06T16:17:28Z',
                updated_at = '2014-11-06T16:17:28Z',
                closed_at = '2014-11-06T16:17:28Z',
                item_count = 1,
                yes_item_count = 1,
                personal = True,
                item_total = 1,
                conforming_item_count = 1,
                deficient_item_count = 1,
                na_item_count = 0,
                neutral_item_count = 1,
                not_inspected_item_count = 0,
                drawing_ids = [
                    56
                    ],
                current_drawing_revision_ids = [
                    56
                    ],
                location = procore_sdk.models.location.Location(
                    id = 15504, 
                    name = '1space>1 space', 
                    node_name = '1 space', 
                    parent_id = 788866, 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', ),
                specification_section = procore_sdk.models.checklist_3_specification_section.Checklist_3_specification_section(
                    id = 56, 
                    description = '', 
                    section = '', 
                    latest_revision_url = '', ),
                trade = procore_sdk.models.trade.Trade(
                    id = 999, 
                    name = '09 - acoustical panels', 
                    active = True, 
                    updated_at = '2016-08-01T23:33:54Z', ),
                created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                    id = 160586, 
                    login = 'exampleuser@example.com', 
                    name = 'Carl Contractor', ),
                closed_by = procore_sdk.models.checklist_closed_by.Checklist_closed_by(
                    id = 160586, 
                    login = 'exampleuser@example.com', 
                    name = 'Carl Contractor', ),
                inspectors = [
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
                            attachment = procore_sdk.models.checklist_signature_3_attachment.Checklist_Signature_3_attachment(
                                id = 5324, 
                                thumbnail_url = 'http://www.example.com/', 
                                url = 'http://www.example.com/', 
                                filename = 'january_receipt_copy.jpg', 
                                name = 'january_receipt_copy.jpg', 
                                viewable_document_id = 492, ), ), )
                    ],
                responsible_contractor = procore_sdk.models.checklist_3_responsible_contractor.Checklist_3_responsible_contractor(
                    id = 56, 
                    name = '', ),
                responsible_party = procore_sdk.models.checklist_closed_by.Checklist_closed_by(
                    id = 160586, 
                    login = 'exampleuser@example.com', 
                    name = 'Carl Contractor', ),
                response_set = procore_sdk.models.checklist_default_response_set.ChecklistDefaultResponseSet(
                    conforming_response = 'Pass', 
                    deficient_response = 'Fail', 
                    global = True, 
                    updated_at = '2014-11-06T16:17:28Z', 
                    created_at = '2014-11-06T16:17:28Z', ),
                attachments = [
                    procore_sdk.models.checklist_3_attachments_inner.Checklist_3_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        filename = 'january_receipt_copy.jpg', 
                        name = 'january_receipt_copy.jpg', )
                    ],
                sections = [
                    procore_sdk.models.checklist_section.Checklist Section(
                        id = 21, 
                        name = 'Framing', 
                        position = 1, 
                        origin_id = 3, 
                        items = [
                            procore_sdk.models.checklist_section_item.Checklist Section Item(
                                id = 2, 
                                name = 'Item 1', 
                                details = '+/- 1 degrees', 
                                status = 'yes', 
                                responded_with = 'Safe - Knowledge', 
                                origin_id = 1, 
                                section_id = 21, 
                                position = 1, 
                                observations = [
                                    procore_sdk.models.checklist_section_item_observations_inner.Checklist_Section_Item_observations_inner(
                                        id = 2085, 
                                        created_at = '2012-10-23T21:39:40Z', 
                                        number = '56', 
                                        status = 'initiated', 
                                        title = 'Clean up paint splatter', 
                                        type = procore_sdk.models.checklist_section_item_observations_inner_type.Checklist_Section_Item_observations_inner_type(
                                            id = 4952, 
                                            name = 'Deficiency', 
                                            active = True, ), 
                                        assignee = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                                            id = 160586, 
                                            login = 'exampleuser@example.com', 
                                            name = 'Carl Contractor', ), 
                                        created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                                            id = 160586, 
                                            login = 'exampleuser@example.com', 
                                            name = 'Carl Contractor', ), )
                                    ], 
                                attachment_histories = [
                                    procore_sdk.models.checklist_section_item_attachment_histories_inner.Checklist_Section_Item_attachment_histories_inner(
                                        id = 6485, 
                                        created_at = '2012-10-23T21:39:40Z', 
                                        attachment = procore_sdk.models.checklist_signature_1_attachment.Checklist_Signature_1_attachment(
                                            id = 5324, 
                                            url = 'http://www.example.com/', 
                                            filename = 'january_receipt_copy.jpg', 
                                            name = 'january_receipt_copy.jpg', ), )
                                    ], 
                                attachments = [
                                    procore_sdk.models.checklist_section_item_attachment_histories_inner.Checklist_Section_Item_attachment_histories_inner(
                                        id = 6485, 
                                        created_at = '2012-10-23T21:39:40Z', )
                                    ], 
                                histories = [
                                    procore_sdk.models.checklist_section_item_histories_inner.Checklist_Section_Item_histories_inner(
                                        id = 56, 
                                        body = 'changed the status to yes', 
                                        status = 'yes', 
                                        responded_with = 'Safe - Knowledge', 
                                        created_at = '2012-10-23T21:39:40Z', )
                                    ], 
                                item_response = procore_sdk.models.checklist_item_response.ChecklistItemResponse(
                                    item_id = 4323, 
                                    status = 'conforming', 
                                    responded_at = '2018-10-23T21:39:40Z', 
                                    responder = , 
                                    item_type = procore_sdk.models.checklist_item_type.ChecklistItemType(
                                        id = 1, 
                                        category = 'multiple_choice', 
                                        name = 'default', ), 
                                    payload = procore_sdk.models.checklist_item_response_payload.ChecklistItemResponse_payload(
                                        text_value = 'Supplies arrived at 10:00 AM', 
                                        number_value = 4232, 
                                        date_value = 'Sun Jan 20 00:00:00 UTC 2019', 
                                        response_option = procore_sdk.models.checklist_item_response_payload_response_option.ChecklistItemResponse_payload_response_option(
                                            id = 3432, 
                                            name = 'Safe', ), ), ), 
                                comments = [
                                    procore_sdk.models.checklist_section_item_comments_inner.Checklist_Section_Item_comments_inner(
                                        id = 4798, 
                                        body = 'Paint splatter is also on the top panel of the frame.', 
                                        created_at = '2012-10-23T21:39:40Z', )
                                    ], 
                                response = procore_sdk.models.checklist_response.ChecklistResponse(
                                    id = 1, 
                                    name = 'Safe - Knowledge', 
                                    corresponding_status = 'yes', ), 
                                response_set = procore_sdk.models.checklist_section_item_response_set.Checklist_Section_Item_response_set(
                                    id = 83, 
                                    name = 'Safety Responses', 
                                    responses = [
                                        procore_sdk.models.checklist_response.ChecklistResponse(
                                            id = 1, 
                                            name = 'Safe - Knowledge', 
                                            corresponding_status = 'yes', )
                                        ], 
                                    created_at = '2014-11-06T16:17:28Z', 
                                    updated_at = '2014-11-06T16:17:28Z', ), 
                                type = procore_sdk.models.checklist_item_type.ChecklistItemType(
                                    id = 1, 
                                    category = 'multiple_choice', 
                                    name = 'default', ), 
                                response_set_id = 72, 
                                template_item_id = 34, 
                                response_type_id = 2, )
                            ], 
                        template_section_id = 234, )
                    ],
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
                managed_equipment_id = 234,
                template_id = 12,
                list_template_name = 'Test Checklist',
                trade_id = 288,
                inspection_type_id = 76
            )
        else:
            return Checklist3(
        )
        """

    def testChecklist3(self):
        """Test Checklist3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
