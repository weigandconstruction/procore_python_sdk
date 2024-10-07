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

from procore_sdk.models.rest_v10_projects_project_id_rfis_get200_response_inner import RestV10ProjectsProjectIdRfisGet200ResponseInner

class TestRestV10ProjectsProjectIdRfisGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdRfisGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdRfisGet200ResponseInner:
        """Test RestV10ProjectsProjectIdRfisGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdRfisGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdRfisGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdRfisGet200ResponseInner(
                created_by = None,
                link = 'https://app.procore.com/123456/project/rfi/show/123456',
                location_id = 999,
                questions = [
                    procore_sdk.models.rest_v10_projects_project_id_rfis_get_200_response_inner_all_of_questions_inner.RestV10ProjectsProjectIdRfisGet_200_response_inner_allOf_questions_inner(
                        id = 999, 
                        body = '<p>Are the items listed on Schedule C acceptable?</p>', 
                        errors = [
                            procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_post_403_response.RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPost_403_response()
                            ], )
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
                id = 999,
                assignee = None,
                assignees = [
                    null
                    ],
                ball_in_court = None,
                ball_in_courts = [
                    null
                    ],
                cost_code = procore_sdk.models.timecard_entry_full_cost_code.TimecardEntry_full_cost_code(
                    id = 12345, 
                    name = 'Earthwork', ),
                cost_impact = procore_sdk.models.rest_v10_projects_project_id_rfis_get_200_response_inner_all_of_cost_impact.RestV10ProjectsProjectIdRfisGet_200_response_inner_allOf_cost_impact(
                    status = 'yes_known', 
                    value = 12039.55, ),
                created_at = '2016-08-23T15:23:57Z',
                deleted = True,
                deleted_at = '2016-08-23T15:23:57Z',
                due_date = 'Wed Jan 18 00:00:00 UTC 2017',
                initiated_at = '2016-08-23T15:23:57Z',
                location = procore_sdk.models.location.Location(
                    id = 15504, 
                    name = '1space>1 space', 
                    node_name = '1 space', 
                    parent_id = 788866, 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', ),
                full_number = 'C-1477',
                number = '1477',
                prefix = 'C',
                private = True,
                project_stage = procore_sdk.models.rest_v10_projects_project_id_rfis_get_200_response_inner_all_of_project_stage.RestV10ProjectsProjectIdRfisGet_200_response_inner_allOf_project_stage(
                    id = 12345, 
                    default_stage = True, 
                    dependent_projects = 0, 
                    formatted_name = 'Course of Construction', 
                    formatted_parent_name = 'Course of Construction', 
                    name = 'Course of Construction', 
                    parent_id = 12345, 
                    procore_category = False, ),
                received_from = None,
                reference = 'Schedule C',
                responsible_contractor = procore_sdk.models.rest_v10_projects_project_id_waste_logs_get_200_response_inner_vendor.RestV10ProjectsProjectIdWasteLogsGet_200_response_inner_vendor(
                    id = 161072, 
                    name = 'SID Architecture', ),
                rfi_manager = None,
                schedule_impact = procore_sdk.models.rest_v10_projects_project_id_rfis_get_200_response_inner_all_of_schedule_impact.RestV10ProjectsProjectIdRfisGet_200_response_inner_allOf_schedule_impact(
                    status = 'yes_known', 
                    value = 14, ),
                status = 'open',
                translated_status = 'Abierto',
                sub_job = procore_sdk.models.timecard_entry_3_sub_job.TimecardEntry_3_sub_job(
                    id = 3483483, 
                    name = 'Floor 2', 
                    code = '18', ),
                subject = 'Specifications [99 14.44B]',
                time_resolved = '2017-01-12T17:09:15Z',
                updated_at = '2012-10-24T21:39:40Z'
            )
        else:
            return RestV10ProjectsProjectIdRfisGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdRfisGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdRfisGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
