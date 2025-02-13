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

from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get200_response_inner import RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner

class TestRestV10ProjectsProjectIdManpowerLogsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner(
                id = 333675,
                created_at = '2012-10-23T21:39:40Z',
                var_date = 'Thu May 19 00:00:00 UTC 2016',
                datetime = '2016-05-19T12:00Z',
                deleted_at = '2017-07-29T21:39:40Z',
                man_hours = '32.0',
                notes = 'Manpower Notes',
                num_workers = 4,
                num_hours = '8.0',
                position = 11241,
                status = 'pending',
                updated_at = '2012-10-24T21:39:40Z',
                vendor = procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get_200_response_inner_vendor.RestV10ProjectsProjectIdManpowerLogsGet_200_response_inner_vendor(
                    id = 324, 
                    name = 'AAA Constructions', ),
                user = procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get_200_response_inner_user.RestV10ProjectsProjectIdManpowerLogsGet_200_response_inner_user(
                    id = 324, 
                    login = 'login@example.com', 
                    name = 'AAA Constructions', ),
                contact = procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get_200_response_inner_contact.RestV10ProjectsProjectIdManpowerLogsGet_200_response_inner_contact(
                    id = 1128828, 
                    business_phone = '(503)744-3200', 
                    business_phone_extension = 1234, 
                    email = 'john.doe@example.com', 
                    fax_number = '813043', 
                    job_title = 'Engineer', 
                    login_information_id = 56, 
                    mobile_phone = '', 
                    name = 'A-1 Electric Company', 
                    vendor_name = '', ),
                cost_code = procore_sdk.models.timecard_entry_full_cost_code.TimecardEntry_full_cost_code(
                    id = 12345, 
                    name = 'Earthwork', ),
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                location = procore_sdk.models.location.Location(
                    id = 15504, 
                    name = 'North Building>First Floor>Electrical Closet', 
                    node_name = 'Electrical Closet', 
                    parent_id = 788866, 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', ),
                attachments = [
                    procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get_200_response_inner_attachments_inner.RestV10CompaniesCompanyIdWorkflowPermanentLogsGet_200_response_inner_attachments_inner(
                        id = 56, 
                        name = '', 
                        url = '', 
                        filename = '', )
                    ],
                trade = procore_sdk.models.trade.Trade(
                    id = 999, 
                    name = '09 - acoustical panels', 
                    active = True, 
                    updated_at = '2016-08-01T23:33:54Z', ),
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
                permissions = procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get_200_response_inner_permissions.RestV10ProjectsProjectIdVisitorLogsGet_200_response_inner_permissions(
                    can_update = True, 
                    can_delete = False, )
            )
        else:
            return RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdManpowerLogsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
