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

from procore_sdk.models.rest_v10_projects_project_id_prime_change_orders_post201_response import RestV10ProjectsProjectIdPrimeChangeOrdersPost201Response

class TestRestV10ProjectsProjectIdPrimeChangeOrdersPost201Response(unittest.TestCase):
    """RestV10ProjectsProjectIdPrimeChangeOrdersPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdPrimeChangeOrdersPost201Response:
        """Test RestV10ProjectsProjectIdPrimeChangeOrdersPost201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdPrimeChangeOrdersPost201Response`
        """
        model = RestV10ProjectsProjectIdPrimeChangeOrdersPost201Response()
        if include_optional:
            return RestV10ProjectsProjectIdPrimeChangeOrdersPost201Response(
                attachments = [
                    procore_sdk.models.default_2_attachments_inner.default_2_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        name = 'january_receipt_copy.jpg', )
                    ],
                id = 34219,
                batch_id = 34219,
                contract_id = 45121,
                legacy_package_id = 34219,
                legacy_request_id = 34219,
                location_id = 34219,
                description = '<p>Change order description</p>',
                title = 'ABC Prime Change Order',
                invoiced_date = 'Fri May 14 00:00:00 UTC 2021',
                paid_date = 'Fri May 14 00:00:00 UTC 2021',
                due_date = 'Fri May 14 00:00:00 UTC 2021',
                revised_substantial_completion_date = 'Thu May 13 00:00:00 UTC 2021',
                signed_change_order_received_date = 'Sun Oct 23 00:00:00 UTC 2016',
                updated_at = '2016-10-26T21:43:40Z',
                created_at = '2017-08-14T21:39:40Z',
                reviewed_at = '2022-10-26T21:43:40Z',
                executed = True,
                paid = True,
                signature_required = False,
                private = True,
                field_change = True,
                grand_total = '23474.0',
                schedule_impact_amount = 5,
                number = 'H-38',
                type = 'PrimeChangeOrder',
                revision = 1,
                status = 'draft',
                reference = 'Reference',
                created_by = procore_sdk.models.default_1_created_by.default_1_created_by(
                    id = 161072, 
                    name = 'Carl the Contractor', ),
                designated_reviewer = procore_sdk.models.default_1_designated_reviewer.default_1_designated_reviewer(
                    id = 161072, 
                    name = 'Carl the Contractor', ),
                received_from = procore_sdk.models.default_1_received_from.default_1_received_from(
                    id = 161072, 
                    name = 'Carl the Contractor', ),
                reviewed_by = procore_sdk.models.default_1_reviewed_by.default_1_reviewed_by(
                    id = 161072, 
                    name = 'Carl the Contractor', ),
                change_order_change_reason = procore_sdk.models.default_1_change_order_change_reason.default_1_change_order_change_reason(
                    id = 161072, 
                    change_reason = 'Change reason value', ),
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
                currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                    currency_iso_code = 'USD', ),
                change_events = [
                    procore_sdk.models.extended_3_change_events_inner.extended_3_change_events_inner(
                        id = 161072, 
                        number = '123', )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdPrimeChangeOrdersPost201Response(
        )
        """

    def testRestV10ProjectsProjectIdPrimeChangeOrdersPost201Response(self):
        """Test RestV10ProjectsProjectIdPrimeChangeOrdersPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
