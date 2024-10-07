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

from procore_sdk.models.rest_v10_projects_project_id_delivery_logs_post_request import RestV10ProjectsProjectIdDeliveryLogsPostRequest

class TestRestV10ProjectsProjectIdDeliveryLogsPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdDeliveryLogsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDeliveryLogsPostRequest:
        """Test RestV10ProjectsProjectIdDeliveryLogsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDeliveryLogsPostRequest`
        """
        model = RestV10ProjectsProjectIdDeliveryLogsPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdDeliveryLogsPostRequest(
                delivery_log = procore_sdk.models.rest_v10_projects_project_id_delivery_logs_post_request_delivery_log.RestV10ProjectsProjectIdDeliveryLogsPost_request_delivery_log(
                    comments = '', 
                    contents = '', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    datetime = '2016-05-19T12:00Z', 
                    delivery_from = '', 
                    time_hour = 0, 
                    time_minute = 0, 
                    tracking_number = '', )
            )
        else:
            return RestV10ProjectsProjectIdDeliveryLogsPostRequest(
                delivery_log = procore_sdk.models.rest_v10_projects_project_id_delivery_logs_post_request_delivery_log.RestV10ProjectsProjectIdDeliveryLogsPost_request_delivery_log(
                    comments = '', 
                    contents = '', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    datetime = '2016-05-19T12:00Z', 
                    delivery_from = '', 
                    time_hour = 0, 
                    time_minute = 0, 
                    tracking_number = '', ),
        )
        """

    def testRestV10ProjectsProjectIdDeliveryLogsPostRequest(self):
        """Test RestV10ProjectsProjectIdDeliveryLogsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
