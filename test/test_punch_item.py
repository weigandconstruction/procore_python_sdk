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

from procore_sdk.models.punch_item import PunchItem

class TestPunchItem(unittest.TestCase):
    """PunchItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PunchItem:
        """Test PunchItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PunchItem`
        """
        model = PunchItem()
        if include_optional:
            return PunchItem(
                id = 83978,
                ball_in_court = [
                    procore_sdk.models.punch_item_ball_in_court_inner.Punch_Item_ball_in_court_inner(
                        id = 1738090, 
                        name = 'John Doe', 
                        locale = 'ko', )
                    ],
                closed_at = '2012-10-23T21:39:40Z',
                cost_impact = 'yes_known',
                cost_impact_amount = '100.0',
                created_at = '2012-10-23T21:39:40Z',
                deleted_at = '2017-07-29T21:39:40Z',
                description = '',
                due_date = 'Mon Sep 30 00:00:00 UTC 2013',
                name = 'test 1 today',
                reference = '3A',
                schedule_impact = 'yes_known',
                schedule_impact_days = 3,
                schedule_risk = 'ml_high',
                schedule_risk_reason = '',
                schedule_risk_confidence = 90,
                schedule_risk_probability = 90,
                position = 1,
                priority = '',
                private = False,
                status = 'Open',
                has_resolved_responses = True,
                has_unresolved_responses = True,
                updated_at = '2012-10-24T21:39:40Z',
                location = procore_sdk.models.location.Location(
                    id = 15504, 
                    name = 'North Building>First Floor>Electrical Closet', 
                    node_name = 'Electrical Closet', 
                    parent_id = 788866, 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', 
                    code = 'L1', ),
                trade = procore_sdk.models.trade.Trade(
                    id = 999, 
                    name = '09 - acoustical panels', 
                    active = True, 
                    updated_at = '2016-08-01T23:33:54Z', ),
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                punch_item_manager = procore_sdk.models.punch_item_ball_in_court_inner.Punch_Item_ball_in_court_inner(
                    id = 1738090, 
                    name = 'John Doe', 
                    locale = 'ko', ),
                final_approver = procore_sdk.models.punch_item_ball_in_court_inner.Punch_Item_ball_in_court_inner(
                    id = 1738090, 
                    name = 'John Doe', 
                    locale = 'ko', ),
                punch_item_type = procore_sdk.models.punch_item_type.Punch Item Type(
                    id = 44165, 
                    name = 'Extra Work', ),
                cost_code = procore_sdk.models.timecard_entry_full_cost_code.TimecardEntry_full_cost_code(
                    id = 12345, 
                    name = 'Earthwork', ),
                assignments = [
                    procore_sdk.models.punch_item_assignments_inner.Punch_Item_assignments_inner(
                        id = 333675, 
                        approved = True, 
                        comment = 'Completed', 
                        login_information_id = 420, 
                        login_information_name = 'Edgar Admin', 
                        login_information = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                            id = 160586, 
                            login = 'carl.contractor@example.com', 
                            name = 'Carl Contractor', ), 
                        attachments = [
                            procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                                id = 5324, 
                                url = 'http://www.example.com/', 
                                filename = 'january_receipt_copy.jpg', )
                            ], 
                        vendor = procore_sdk.models.compact.Compact(
                            id = 161072, 
                            name = 'SID Architecture', ), 
                        notified_at = '2018-06-25T22:22:42Z', 
                        responded_at = '2018-06-25T22:22:42Z', 
                        status = 'unresolved', 
                        manager_accepted_at = '2018-10-26T18:15:26Z', 
                        user_name = 'Edgar Admin', 
                        updated_at = '2018-10-26T18:15:26Z', )
                    ],
                assignees = [
                    procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                        id = 160586, 
                        login = 'carl.contractor@example.com', 
                        name = 'Carl Contractor', )
                    ],
                workflow_status = 'initiated',
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
                        data_type = 'lov_entries', ), )
            )
        else:
            return PunchItem(
        )
        """

    def testPunchItem(self):
        """Test PunchItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
