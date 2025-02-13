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

from procore_sdk.models.rest_v10_projects_project_id_incidents_near_misses_post_request import RestV10ProjectsProjectIdIncidentsNearMissesPostRequest

class TestRestV10ProjectsProjectIdIncidentsNearMissesPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdIncidentsNearMissesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdIncidentsNearMissesPostRequest:
        """Test RestV10ProjectsProjectIdIncidentsNearMissesPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdIncidentsNearMissesPostRequest`
        """
        model = RestV10ProjectsProjectIdIncidentsNearMissesPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdIncidentsNearMissesPostRequest(
                near_miss = procore_sdk.models.incident_near_miss_create_parameters.IncidentNearMissCreateParameters(
                    incident_id = 56, 
                    description = '<p>Sprain to <b>Hand</b> by Ground</p>', 
                    affected_person_id = 56, 
                    affected_party_id = 56, 
                    harm_source_id = 56, 
                    affected_company_id = 56, 
                    managed_equipment_id = 56, 
                    work_activity_id = 56, 
                    custom_field_%{custom_field_definition_id} = custom field value, )
            )
        else:
            return RestV10ProjectsProjectIdIncidentsNearMissesPostRequest(
                near_miss = procore_sdk.models.incident_near_miss_create_parameters.IncidentNearMissCreateParameters(
                    incident_id = 56, 
                    description = '<p>Sprain to <b>Hand</b> by Ground</p>', 
                    affected_person_id = 56, 
                    affected_party_id = 56, 
                    harm_source_id = 56, 
                    affected_company_id = 56, 
                    managed_equipment_id = 56, 
                    work_activity_id = 56, 
                    custom_field_%{custom_field_definition_id} = custom field value, ),
        )
        """

    def testRestV10ProjectsProjectIdIncidentsNearMissesPostRequest(self):
        """Test RestV10ProjectsProjectIdIncidentsNearMissesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
