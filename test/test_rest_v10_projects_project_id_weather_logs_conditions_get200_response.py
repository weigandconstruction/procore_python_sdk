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

from procore_sdk.models.rest_v10_projects_project_id_weather_logs_conditions_get200_response import RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response

class TestRestV10ProjectsProjectIdWeatherLogsConditionsGet200Response(unittest.TestCase):
    """RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response:
        """Test RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response`
        """
        model = RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response()
        if include_optional:
            return RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response(
                sky = [
                    ''
                    ],
                ground = [
                    ''
                    ],
                calamity = [
                    ''
                    ],
                wind = [
                    ''
                    ],
                temperature = [
                    ''
                    ]
            )
        else:
            return RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response(
        )
        """

    def testRestV10ProjectsProjectIdWeatherLogsConditionsGet200Response(self):
        """Test RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
