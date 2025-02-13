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

from procore_sdk.models.rest_v10_projects_project_id_incidents_post_request_incident import RestV10ProjectsProjectIdIncidentsPostRequestIncident

class TestRestV10ProjectsProjectIdIncidentsPostRequestIncident(unittest.TestCase):
    """RestV10ProjectsProjectIdIncidentsPostRequestIncident unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdIncidentsPostRequestIncident:
        """Test RestV10ProjectsProjectIdIncidentsPostRequestIncident
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdIncidentsPostRequestIncident`
        """
        model = RestV10ProjectsProjectIdIncidentsPostRequestIncident()
        if include_optional:
            return RestV10ProjectsProjectIdIncidentsPostRequestIncident(
                description = 'Can of gasoline tipped over near drying cement.',
                event_date = '2016-10-25T17:53:35Z',
                distribution_member_ids = [
                    56
                    ],
                private = False,
                recordable = False,
                status = 'open',
                time_unknown = False,
                title = 'HAZMAT Spill',
                contributing_behavior_id = 56,
                contributing_condition_id = 56,
                hazard_id = 56,
                location_id = 56,
                environmentals = [
                    procore_sdk.models.incident_environmental_update_parameters.IncidentEnvironmentalUpdateParameters(
                        environmental_type_id = 56, 
                        description = '<p>Sprain to <b>Hand</b> by Ground</p>', 
                        estimated_cost_impact = 20000, 
                        quantity_value = 1000, 
                        quantity_unit_of_measure = 'Lbs', 
                        affected_company_id = 56, 
                        managed_equipment_id = 56, 
                        work_activity_id = 56, 
                        custom_field_%{custom_field_definition_id} = custom field value, )
                    ],
                injuries = [
                    procore_sdk.models.incident_injury_update_parameters.IncidentInjuryUpdateParameters(
                        date_of_death = '2016-10-25T17:53:35Z', 
                        description = '<p>Sprain to <b>Hand</b> by Ground</p>', 
                        filing_type = 'first_aid', 
                        hospitalized_overnight = True, 
                        recordable = True, 
                        treated_in_er = True, 
                        treatment_facility_address = '6309 Carpinteria Ave.', 
                        treatment_facility = 'Procore Hospital', 
                        treatment_provider = 'Dr. Doctor', 
                        work_days_absent = 1, 
                        work_days_restricted = 3, 
                        work_days_transferred = 4, 
                        affliction_type_id = 56, 
                        body_diagram_type = 'feminine', 
                        affected_body_parts = [
                            'abdomen'
                            ], 
                        affected_person_id = 56, 
                        affected_party_id = 56, 
                        body_part_ids = [
                            1
                            ], 
                        harm_source_id = 56, 
                        affected_company_id = 56, 
                        managed_equipment_id = 56, 
                        work_activity_id = 56, 
                        custom_field_%{custom_field_definition_id} = custom field value, )
                    ],
                near_misses = [
                    procore_sdk.models.incident_near_miss_update_parameters.IncidentNearMissUpdateParameters(
                        description = '<p>Sprain to <b>Hand</b> by Ground</p>', 
                        affected_person_id = 56, 
                        affected_party_id = 56, 
                        harm_source_id = 56, 
                        affected_company_id = 56, 
                        managed_equipment_id = 56, 
                        work_activity_id = 56, 
                        custom_field_%{custom_field_definition_id} = custom field value, )
                    ],
                property_damages = [
                    procore_sdk.models.incident_property_damage_update_parameters.IncidentPropertyDamageUpdateParameters(
                        description = '<p>Sprain to <b>Hand</b> by Ground</p>', 
                        estimated_cost_impact = 20000, 
                        affected_company_id = 56, 
                        responsible_company_id = 56, 
                        managed_equipment_id = 56, 
                        work_activity_id = 56, 
                        custom_field_%{custom_field_definition_id} = custom field value, )
                    ],
                witness_statements_attributes = [
                    procore_sdk.models.incident_witness_statement_update_parameters.IncidentWitnessStatementUpdateParameters(
                        statement = '<p>I witnessed what happened.</p>', 
                        date_received = 'Tue Oct 25 00:00:00 UTC 2016', 
                        witness_id = 1, 
                        custom_field_%{custom_field_definition_id} = custom field value, )
                    ],
                upload_uuids = [
                    '1ZE258W9K804SAJJZX19JVAB3R'
                    ],
                custom_field_custom_field_definition_id = custom field value,
                drawing_revision_ids = [4,5],
                file_version_ids = [6,7],
                form_ids = [7,8],
                image_ids = [9,10]
            )
        else:
            return RestV10ProjectsProjectIdIncidentsPostRequestIncident(
        )
        """

    def testRestV10ProjectsProjectIdIncidentsPostRequestIncident(self):
        """Test RestV10ProjectsProjectIdIncidentsPostRequestIncident"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
