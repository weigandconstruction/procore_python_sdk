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

from procore_sdk.models.incident_normal_all_of_injuries_inner import IncidentNormalAllOfInjuriesInner

class TestIncidentNormalAllOfInjuriesInner(unittest.TestCase):
    """IncidentNormalAllOfInjuriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IncidentNormalAllOfInjuriesInner:
        """Test IncidentNormalAllOfInjuriesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IncidentNormalAllOfInjuriesInner`
        """
        model = IncidentNormalAllOfInjuriesInner()
        if include_optional:
            return IncidentNormalAllOfInjuriesInner(
                type = 'injury',
                date_returned_to_work = 'Wed Oct 31 00:00:00 UTC 2018',
                affected_party = procore_sdk.models.party.Party(
                    id = 1, 
                    name = 'Dolores Umbridge', ),
                affected_person = None,
                harm_source = procore_sdk.models.harm_source.Harm Source(
                    id = 999, 
                    name = 'Material', 
                    active = True, 
                    global = True, 
                    created_at = '2016-10-25T17:53:35Z', 
                    updated_at = '2016-10-25T17:53:35Z', ),
                date_of_death = 'Sat Nov 10 00:00:00 UTC 2018',
                filing_type = 'first_aid',
                hospitalized_overnight = True,
                treated_in_er = True,
                treatment_facility_address = '6309 Carpinteria Ave.',
                treatment_facility = 'Procore Hospital',
                treatment_provider = 'Dr. Doctor',
                work_days_absent = 1,
                work_days_restricted = 3,
                work_days_transferred = 4,
                body_diagram_type = 'feminine',
                affliction_type = procore_sdk.models.affliction_type.Affliction Type(
                    id = 999, 
                    name = 'Sprain', 
                    active = True, 
                    global = True, 
                    created_at = '2016-10-25T17:53:35Z', 
                    updated_at = '2016-10-25T17:53:35Z', ),
                affected_body_part = 'ankle',
                affected_body_parts = [
                    'ankle'
                    ],
                afflictions = [
                    procore_sdk.models.incident_affliction.IncidentAffliction(
                        id = 999, 
                        affliction_type = procore_sdk.models.affliction_type.Affliction Type(
                            id = 999, 
                            name = 'Sprain', 
                            active = True, 
                            global = True, 
                            created_at = '2016-10-25T17:53:35Z', 
                            updated_at = '2016-10-25T17:53:35Z', ), 
                        affected_body_part = 'ankle', )
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
                body_parts = [
                    procore_sdk.models.body_part.Body Part(
                        id = 999, 
                        name = 'finger_index_right', 
                        selectable = True, 
                        created_at = '2016-10-25T17:53:35Z', 
                        updated_at = '2016-10-25T17:53:35Z', 
                        parent_id = 999, )
                    ],
                id = 9,
                number = 4,
                full_number = '16.4',
                incident_id = 16,
                recordable = True,
                incident_title = 'HAZMAT Spill',
                incident_private = False,
                summary = 'Sprain to Hand by Ground / Floor. Note: This key has been deprecated.',
                description_plain_text = 'Sprain to Hand by Ground',
                description = '<p>Sprain to <b>Hand</b> by Ground</p>',
                affected_company = procore_sdk.models.rest_v10_projects_project_id_waste_logs_get_200_response_inner_vendor.RestV10ProjectsProjectIdWasteLogsGet_200_response_inner_vendor(
                    id = 161072, 
                    name = 'SID Architecture', ),
                created_at = '2016-10-25T17:53:35Z',
                deleted_at = '2016-10-25T17:53:35Z',
                managed_equipment = procore_sdk.models.incident_normal_all_of_environmentals_inner_all_of_managed_equipment.IncidentNormal_allOf_environmentals_inner_allOf_managed_equipment(
                    id = 15504, 
                    name = 'Jackhammer', ),
                incident_created_by = None,
                updated_at = '2016-10-25T17:53:35Z',
                work_activity = procore_sdk.models.work_activity.Work Activity(
                    id = 999, 
                    name = 'Earthwork', 
                    active = True, 
                    global = True, 
                    created_at = '2016-10-25T17:53:35Z', 
                    updated_at = '2015-11-12T21:26:28Z', )
            )
        else:
            return IncidentNormalAllOfInjuriesInner(
        )
        """

    def testIncidentNormalAllOfInjuriesInner(self):
        """Test IncidentNormalAllOfInjuriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
