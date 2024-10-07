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

from procore_sdk.models.rest_v10_change_order_packages_id_get200_response import RestV10ChangeOrderPackagesIdGet200Response

class TestRestV10ChangeOrderPackagesIdGet200Response(unittest.TestCase):
    """RestV10ChangeOrderPackagesIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ChangeOrderPackagesIdGet200Response:
        """Test RestV10ChangeOrderPackagesIdGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ChangeOrderPackagesIdGet200Response`
        """
        model = RestV10ChangeOrderPackagesIdGet200Response()
        if include_optional:
            return RestV10ChangeOrderPackagesIdGet200Response(
                id = 239475,
                contract_id = 64545,
                created_at = '2016-10-23T21:39:40Z',
                deleted_at = '2016-10-27T21:39:40Z',
                description = 'Additional Time & Materials for October',
                due_date = 'Sun Oct 23 00:00:00 UTC 2016',
                executed = True,
                grand_total = '23474.0',
                invoiced_date = 'Wed Oct 26 00:00:00 UTC 2016',
                number = 'H-38',
                origin_code = 'ABC-123',
                origin_data = 'OD-123654789',
                origin_id = '654987123',
                paid_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                position = 4,
                private = True,
                review_notes = 'Make sure Jon sees this before proceeding',
                reviewed_at = '2016-10-24T15:42:33Z',
                revised_substantial_completion_date = 'Mon Oct 30 00:00:00 UTC 2017',
                revision = 1,
                schedule_impact_amount = 5,
                signed_change_order_received_date = 'Sun Oct 23 00:00:00 UTC 2016',
                status = 'draft',
                title = 'Additional Time & Materials',
                type = 'PrimeContractChangeOrder',
                updated_at = '2016-10-26T21:43:40Z',
                creator = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                designated_reviewer = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                reviewer = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                attachments = [
                    procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get_200_response_inner_attachments_inner.RestV10CompaniesCompanyIdWorkflowPermanentLogsGet_200_response_inner_attachments_inner(
                        id = 56, 
                        name = '', 
                        url = '', 
                        filename = '', )
                    ],
                line_items = [
                    procore_sdk.models.rest_v10_change_order_packages_id_get_200_response_line_items_inner.RestV10ChangeOrderPackagesIdGet_200_response_line_items_inner(
                        id = 453927, 
                        position = 3, 
                        description = 'Extra materials', 
                        quantity = '30.0', 
                        uom = 'lbs', 
                        total_amount = '60.0', 
                        extended_amount = '900.0', 
                        unit_cost = '2.0', 
                        cost_code = null, 
                        wbs_code = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_wbs_code.RestV10WorkOrderContractsPost_201_response_line_items_inner_wbs_code(
                            id = 999, 
                            flat_code = '01-011.CT1', 
                            description = 'Project Engineer.Cost Type 1', ), 
                        holder = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_holder.RestV10WorkOrderContractsPost_201_response_line_items_inner_holder(
                            id = 233245, 
                            holder_type = 'WorkOrderContract', ), 
                        line_item_type = procore_sdk.models.line_item_type.LineItemType(
                            id = 12345, 
                            name = 'Equipment', 
                            code = 'LB', 
                            base_type = 'materials', 
                            origin_data = 'OD-2398273424', 
                            origin_id = 'ABC123', ), 
                        markup_line_items = [
                            procore_sdk.models.rest_v10_change_order_packages_id_get_200_response_line_items_inner_markup_line_items_inner.RestV10ChangeOrderPackagesIdGet_200_response_line_items_inner_markup_line_items_inner(
                                id = 352362, 
                                amount = '', 
                                created_at = '2017-08-14T21:39:40Z', 
                                updated_at = '2017-08-14T21:39:40Z', 
                                markup = procore_sdk.models.rest_v10_change_order_packages_id_get_200_response_line_items_inner_markup_line_items_inner_markup.RestV10ChangeOrderPackagesIdGet_200_response_line_items_inner_markup_line_items_inner_markup(
                                    id = 462136, 
                                    position = 1, 
                                    markup_set = 'horizontal', 
                                    name = 'Foo', 
                                    percentage = '10', 
                                    compounds_markups_above = False, 
                                    created_at = '2017-08-14T21:39:40Z', 
                                    updated_at = '2017-08-14T21:39:40Z', 
                                    wbs_code_id = 67890, 
                                    destination_cost_code = null, 
                                    destination_line_item_type = procore_sdk.models.line_item_type.LineItemType(
                                        id = 12345, 
                                        name = 'Equipment', 
                                        code = 'LB', 
                                        base_type = 'materials', 
                                        origin_data = 'OD-2398273424', 
                                        origin_id = 'ABC123', ), 
                                    desitination_budget_line_item_id = 362262, 
                                    destination_sub_job = null, ), 
                                currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                                    currency_iso_code = 'USD', ), )
                            ], 
                        currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                            currency_iso_code = 'USD', ), )
                    ],
                currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                    currency_iso_code = 'USD', ),
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
            return RestV10ChangeOrderPackagesIdGet200Response(
        )
        """

    def testRestV10ChangeOrderPackagesIdGet200Response(self):
        """Test RestV10ChangeOrderPackagesIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
