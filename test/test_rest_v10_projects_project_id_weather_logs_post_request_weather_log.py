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

from procore_sdk.models.rest_v10_projects_project_id_weather_logs_post_request_weather_log import RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog

class TestRestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog(unittest.TestCase):
    """RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog:
        """Test RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog`
        """
        model = RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog()
        if include_optional:
            return RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog(
                var_date = 'Thu May 19 00:00:00 UTC 2016',
                is_weather_delay = 1,
                sky = 'Clear',
                temperature = 'Hot',
                average = '50',
                wind = 'Calm',
                ground = 'Dry',
                calamity = 'Fire',
                precipitation = 'Yes minor saturation',
                comments = 'Weather Log Comments',
                time = '15:57:37Z'
            )
        else:
            return RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog(
                var_date = 'Thu May 19 00:00:00 UTC 2016',
        )
        """

    def testRestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog(self):
        """Test RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
