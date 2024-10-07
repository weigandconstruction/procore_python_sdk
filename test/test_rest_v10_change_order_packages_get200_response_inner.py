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

from procore_sdk.models.rest_v10_change_order_packages_get200_response_inner import RestV10ChangeOrderPackagesGet200ResponseInner

class TestRestV10ChangeOrderPackagesGet200ResponseInner(unittest.TestCase):
    """RestV10ChangeOrderPackagesGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ChangeOrderPackagesGet200ResponseInner:
        """Test RestV10ChangeOrderPackagesGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ChangeOrderPackagesGet200ResponseInner`
        """
        model = RestV10ChangeOrderPackagesGet200ResponseInner()
        if include_optional:
            return RestV10ChangeOrderPackagesGet200ResponseInner(
                id = 239475,
                contract_id = 64545,
                created_at = '2016-10-23T21:39:40Z',
                created_by_id = 1,
                deleted_at = '2017-07-29T21:39:40Z',
                due_date = 'Sun Oct 23 00:00:00 UTC 2016',
                executed = True,
                invoiced_date = 'Sun Oct 09 00:00:00 UTC 2016',
                number = 'H-38',
                origin_code = 'ABC-123',
                origin_data = 'OD-123654789',
                origin_id = '654987123',
                paid_date = 'Sat Oct 22 00:00:00 UTC 2016',
                reviewed_at = '2016-10-24T15:42:33Z',
                signed_change_order_received_date = 'Sun Oct 23 00:00:00 UTC 2016',
                status = 'draft',
                title = 'Additional Time & Materials',
                updated_at = '2016-10-23T21:39:40Z',
                revision = 1,
                grand_total = '23474.0',
                designated_reviewer = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
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
            return RestV10ChangeOrderPackagesGet200ResponseInner(
        )
        """

    def testRestV10ChangeOrderPackagesGet200ResponseInner(self):
        """Test RestV10ChangeOrderPackagesGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
