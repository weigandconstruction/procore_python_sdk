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

from procore_sdk.models.rest_v10_projects_project_id_weather_logs_get200_response_inner import RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner

class TestRestV10ProjectsProjectIdWeatherLogsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner(
                id = 20160101,
                attachments = [
                    procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get_200_response_inner_attachments_inner.RestV10CompaniesCompanyIdWorkflowPermanentLogsGet_200_response_inner_attachments_inner(
                        id = 56, 
                        name = '', 
                        url = '', 
                        filename = '', )
                    ],
                average = '50',
                calamity = 'Fire',
                comments = 'Weather Log Comments',
                created_at = '2012-10-23T21:39:40Z',
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                var_date = 'Thu May 19 00:00:00 UTC 2016',
                datetime = '2016-05-19T12:00Z',
                deleted_at = '2017-07-29T21:39:40Z',
                is_weather_delay = '1',
                ground = 'Dry',
                position = 1,
                precipitation = 'true',
                sky = 'Clear',
                temperature = 'Hot',
                time = '2012-10-24T21:39:40Z',
                wind = 'Calm',
                updated_at = '2012-10-24T21:39:40Z'
            )
        else:
            return RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdWeatherLogsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
