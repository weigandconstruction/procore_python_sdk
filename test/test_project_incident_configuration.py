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

from procore_sdk.models.project_incident_configuration import ProjectIncidentConfiguration

class TestProjectIncidentConfiguration(unittest.TestCase):
    """ProjectIncidentConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectIncidentConfiguration:
        """Test ProjectIncidentConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectIncidentConfiguration`
        """
        model = ProjectIncidentConfiguration()
        if include_optional:
            return ProjectIncidentConfiguration(
                project_id = 5,
                private_by_default = True,
                default_distribution = [
                    procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                        id = 160586, 
                        login = 'carl.contractor@example.com', 
                        name = 'Carl Contractor', )
                    ]
            )
        else:
            return ProjectIncidentConfiguration(
        )
        """

    def testProjectIncidentConfiguration(self):
        """Test ProjectIncidentConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
