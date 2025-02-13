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

from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_post_request import RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest

class TestRestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest(unittest.TestCase):
    """RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest:
        """Test RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest`
        """
        model = RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest()
        if include_optional:
            return RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest(
                weather_log = procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_post_request_weather_log.RestV11ProjectsProjectIdDailyLogsWeatherLogsPost_request_weather_log(
                    date = 'Thu May 19 00:00:00 UTC 2016', 
                    is_weather_delay = 1, 
                    calamity = 'Fire', 
                    ground = 'Dry', 
                    sky = 'Clear', 
                    temperature = 'Hot', 
                    wind = 'Calm', 
                    average = '50', 
                    precipitation = 'Yes minor saturation', 
                    comments = 'Weather Log Comments', 
                    time = '15:57:37Z', 
                    drawing_revision_ids = [4,5], 
                    file_version_ids = [6,7], 
                    form_ids = [7,8], 
                    image_ids = [9,10], 
                    upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"], )
            )
        else:
            return RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest(
                weather_log = procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_post_request_weather_log.RestV11ProjectsProjectIdDailyLogsWeatherLogsPost_request_weather_log(
                    date = 'Thu May 19 00:00:00 UTC 2016', 
                    is_weather_delay = 1, 
                    calamity = 'Fire', 
                    ground = 'Dry', 
                    sky = 'Clear', 
                    temperature = 'Hot', 
                    wind = 'Calm', 
                    average = '50', 
                    precipitation = 'Yes minor saturation', 
                    comments = 'Weather Log Comments', 
                    time = '15:57:37Z', 
                    drawing_revision_ids = [4,5], 
                    file_version_ids = [6,7], 
                    form_ids = [7,8], 
                    image_ids = [9,10], 
                    upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"], ),
        )
        """

    def testRestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest(self):
        """Test RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
