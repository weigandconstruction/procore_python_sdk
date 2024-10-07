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

from procore_sdk.models.rest_v11_projects_get200_response_inner import RestV11ProjectsGet200ResponseInner

class TestRestV11ProjectsGet200ResponseInner(unittest.TestCase):
    """RestV11ProjectsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsGet200ResponseInner:
        """Test RestV11ProjectsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsGet200ResponseInner`
        """
        model = RestV11ProjectsGet200ResponseInner()
        if include_optional:
            return RestV11ProjectsGet200ResponseInner(
                id = 89025,
                accounting_project_number = '3456',
                active = True,
                address = '500 Construction Way',
                city = 'Carpinteria',
                company = procore_sdk.models.project_company.ProjectCompany(
                    id = 1234, 
                    name = 'CA Construction', ),
                completion_date = 'Fri May 15 00:00:00 UTC 2015',
                country_code = 'US',
                county = 'Santa Barbara County',
                created_at = '2014-12-29T21:53:56Z',
                custom_fields = procore_sdk.models.normal_custom_fields.normal_custom_fields(
                    custom_field_%{custom_field_boolean_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_boolean_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_boolean_definition_id_(
                        data_type = 'boolean', 
                        value = True, ), 
                    custom_field_%{custom_field_decimal_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_decimal_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_decimal_definition_id_(
                        data_type = 'decimal', 
                        value = 2.2, ), 
                    custom_field_%{custom_field_lov_entries_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_lov_entries_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_lov_entries_definition_id_(
                        data_type = 'lov_entries', 
                        value = [
                            procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_lov_entries_definition_id__value_inner.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_lov_entries_definition_id__value_inner(
                                id = 2, 
                                label = 'Open', )
                            ], ), 
                    custom_field_%{custom_field_lov_entry_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_lov_entry_definition_id_(
                        data_type = 'lov_entry', ), 
                    custom_field_%{custom_field_string_definition_id} = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_custom_fields_custom_field___custom_field_string_definition_id_.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_custom_fields_custom_field___custom_field_string_definition_id_(
                        data_type = 'string', ), ),
                designated_market_area = 'Southeast',
                display_name = 'A-1 Casa de Casper',
                estimated_value = '10000.0',
                is_demo = False,
                latitude = 34.3850464855729,
                longitude = -119.490849121334,
                name = 'Casa de Casper',
                origin_code = 'Code 123',
                origin_data = '459247544',
                origin_id = 'OD-2398273424',
                owners_project_id = 1234,
                parent_job_id = 3,
                phone = '707-555-9866',
                photo_id = 1,
                project_bid_type_id = 1,
                project_number = 'A-1',
                project_owner_type_id = 1,
                project_region_id = 1,
                project_stage = procore_sdk.models.project_stage.ProjectStage(
                    id = 3, 
                    name = 'Course of Construction', ),
                project_template = procore_sdk.models.project_template.ProjectTemplate(
                    id = 3, 
                    name = 'Fairview Apartments', ),
                start_date = 'Fri May 15 00:00:00 UTC 2015',
                state_code = 'CA',
                store_number = '3',
                time_zone = 'US/Pacific',
                total_value = '10000.0',
                updated_at = '2016-03-14T16:52:22Z',
                zip = '93110',
                actual_start_date = 'Fri May 15 00:00:00 UTC 2015',
                departments = [
                    procore_sdk.models.project_department.ProjectDepartment(
                        id = 2, 
                        name = 'Residential', )
                    ],
                description = 'Very cool project.',
                dictionary_type = 'general-contractor',
                estimated_completion_date = 'Sun May 31 00:00:00 UTC 2015',
                estimated_start_date = 'Fri May 15 00:00:00 UTC 2015',
                flag = 'Yellow',
                inbound_email = 'inbound-casa-de-casper',
                logo_url = 'https://s3.amazonaws.com/pro-core.com/prostore/20150904220156_production_105341655.png?AWSAccessKeyId=0PFNH01C4MZVXKXZNK82&Expires=2091808024&Signature=qELZAktHou5QICU747PbcEcN0AY%3D',
                office = procore_sdk.models.project_office.ProjectOffice(
                    id = 3610, 
                    name = 'Carpinteria', ),
                persistent_message = procore_sdk.models.project_persistent_message.ProjectPersistentMessage(
                    message = 'Provide and install HVAC systems.', 
                    title = 'General Scope of Work', ),
                program = procore_sdk.models.project_program.ProjectProgram(
                    id = 4, 
                    name = 'Design Bid', ),
                project_bid_type = procore_sdk.models.project_bid_type.ProjectBidType(
                    id = 1, 
                    name = 'Competitive Bid', ),
                project_owner_type = procore_sdk.models.project_owner_type.ProjectOwnerType(
                    id = 1, 
                    name = 'Project Owner Type A', ),
                project_region = procore_sdk.models.project_region.ProjectRegion(
                    id = 1, 
                    name = 'West', ),
                project_type = procore_sdk.models.project_type.ProjectType(
                    id = 1, 
                    name = 'Project Type A', ),
                projected_finish_date = 'Sun May 31 00:00:00 UTC 2015',
                public_notes = 'We're building a large private residence.',
                square_feet = 5000,
                standard_cost_code_list_id = 1,
                tz_name = 'America/Los_Angeles',
                warranty_end_date = 'Sun May 31 00:00:00 UTC 2015',
                warranty_start_date = 'Fri May 15 00:00:00 UTC 2015'
            )
        else:
            return RestV11ProjectsGet200ResponseInner(
        )
        """

    def testRestV11ProjectsGet200ResponseInner(self):
        """Test RestV11ProjectsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
