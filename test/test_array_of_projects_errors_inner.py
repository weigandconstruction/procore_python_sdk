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

from procore_sdk.models.array_of_projects_errors_inner import ArrayOfProjectsErrorsInner

class TestArrayOfProjectsErrorsInner(unittest.TestCase):
    """ArrayOfProjectsErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayOfProjectsErrorsInner:
        """Test ArrayOfProjectsErrorsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayOfProjectsErrorsInner`
        """
        model = ArrayOfProjectsErrorsInner()
        if include_optional:
            return ArrayOfProjectsErrorsInner(
                id = 89025,
                logo_url = 'https://s3.amazonaws.com/pro-core.com/prostore/20150904220156_production_105341655.png?AWSAccessKeyId=0PFNH01C4MZVXKXZNK82&Expires=2091808024&Signature=qELZAktHou5QICU747PbcEcN0AY%3D',
                name = 'Casa de Casper',
                display_name = 'A-1 Casa de Casper',
                project_number = 'A-1',
                address = '500 Construction Way',
                city = 'Carpinteria',
                state_code = 'CA',
                country_code = 'US',
                zip = '93110',
                time_zone = 'US/Pacific',
                tz_name = 'America/Los_Angeles',
                latitude = 34.3850464855729,
                longitude = -119.490849121334,
                county = 'Santa Barbara County',
                parent_job_id = 3,
                description = 'Very cool project.',
                square_feet = 5000,
                start_date = 'Fri May 15 00:00:00 UTC 2015',
                completion_date = 'Fri May 15 00:00:00 UTC 2015',
                total_value = 10000,
                store_number = '3',
                accounting_project_number = '3456',
                designated_market_area = 'Southeast',
                warranty_start_date = 'Fri May 15 00:00:00 UTC 2015',
                warranty_end_date = 'Sun May 31 00:00:00 UTC 2015',
                active = True,
                flag = 'Yellow',
                phone = '707-555-9866',
                public_notes = 'We're building a large private residence.',
                actual_start_date = 'Fri May 15 00:00:00 UTC 2015',
                projected_finish_date = 'Sun May 31 00:00:00 UTC 2015',
                created_at = '2014-12-29T21:53:56Z',
                updated_at = '2016-03-14T16:52:22Z',
                origin_id = 'OD-2398273424',
                origin_data = '459247544',
                origin_code = 'Code 123',
                standard_cost_code_list_id = 98,
                owners_project_id = 1234,
                photo_id = 1,
                inbound_email = 'inbound-casa-de-casper',
                estimated_start_date = 'Fri May 15 00:00:00 UTC 2015',
                estimated_completion_date = 'Sun May 31 00:00:00 UTC 2015',
                estimated_value = 10000,
                persistent_message = procore_sdk.models.project_persistent_message.ProjectPersistentMessage(
                    title = 'General Scope of Work', 
                    message = 'Provide and install HVAC systems.', ),
                office = procore_sdk.models.project_office.ProjectOffice(
                    id = 3610, 
                    name = 'Carpinteria', 
                    address = '100 Construction Lane', 
                    city = 'Santa Barbara', 
                    state_code = 'CA', 
                    country_code = 'US', 
                    zip = '93101', 
                    phone = '8059831234', 
                    fax = '8059834321', 
                    division = 'First', 
                    logo = procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_get_200_response_inner_attachments_inner.RestV11ProjectsProjectIdDailyLogsWeatherLogsGet_200_response_inner_attachments_inner(
                        id = 56, 
                        name = '', 
                        url = '', ), ),
                project_bid_type = procore_sdk.models.project_bid_type.ProjectBidType(
                    id = 1, 
                    name = 'Competitive Bid', ),
                project_owner_type = procore_sdk.models.project_owner_type.ProjectOwnerType(
                    id = 1, 
                    name = 'Project Owner Type A', ),
                project_region = procore_sdk.models.project_region.ProjectRegion(
                    id = 1, 
                    name = 'West', ),
                project_stage = procore_sdk.models.project_stage.ProjectStage(
                    id = 3, 
                    name = 'Course of Construction', ),
                project_type = procore_sdk.models.project_type.ProjectType(
                    id = 1, 
                    name = 'Project Type A', ),
                program = procore_sdk.models.project_program.ProjectProgram(
                    id = 4, 
                    name = 'Design Bid', ),
                departments = [
                    procore_sdk.models.project_department.ProjectDepartment(
                        id = 2, 
                        name = 'Residential', )
                    ],
                company = procore_sdk.models.project_company.ProjectCompany(
                    id = 1234, 
                    name = 'CA Construction', ),
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
                errors = procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch_200_response_errors_inner_all_of_errors.RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch_200_response_errors_inner_allOf_errors(
                    field_name = [
                        ''
                        ], )
            )
        else:
            return ArrayOfProjectsErrorsInner(
        )
        """

    def testArrayOfProjectsErrorsInner(self):
        """Test ArrayOfProjectsErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
