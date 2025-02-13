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

from procore_sdk.models.rest_v10_projects_project_id_incidents_configuration_patch_request import RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest

class TestRestV10ProjectsProjectIdIncidentsConfigurationPatchRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest:
        """Test RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest`
        """
        model = RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest()
        if include_optional:
            return RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest(
                configuration = procore_sdk.models.rest_v10_projects_project_id_incidents_configuration_patch_request_configuration.RestV10ProjectsProjectIdIncidentsConfigurationPatch_request_configuration(
                    private_by_default = True, 
                    default_distribution_ids = [
                        56
                        ], )
            )
        else:
            return RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest(
                configuration = procore_sdk.models.rest_v10_projects_project_id_incidents_configuration_patch_request_configuration.RestV10ProjectsProjectIdIncidentsConfigurationPatch_request_configuration(
                    private_by_default = True, 
                    default_distribution_ids = [
                        56
                        ], ),
        )
        """

    def testRestV10ProjectsProjectIdIncidentsConfigurationPatchRequest(self):
        """Test RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
