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

from procore_sdk.models.rest_v10_projects_project_id_inspection_logs_post_request import RestV10ProjectsProjectIdInspectionLogsPostRequest

class TestRestV10ProjectsProjectIdInspectionLogsPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdInspectionLogsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdInspectionLogsPostRequest:
        """Test RestV10ProjectsProjectIdInspectionLogsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdInspectionLogsPostRequest`
        """
        model = RestV10ProjectsProjectIdInspectionLogsPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdInspectionLogsPostRequest(
                inspection_log = procore_sdk.models.rest_v10_projects_project_id_inspection_logs_post_request_inspection_log.RestV10ProjectsProjectIdInspectionLogsPost_request_inspection_log(
                    area = 'Level 5', 
                    comments = 'Inspection took a total of 2 hours', 
                    date = 'Thu May 19 00:00:00 UTC 2016', 
                    datetime = '2016-05-19T12:00Z', 
                    end_hour = 10, 
                    end_minute = 0, 
                    inspecting_entity = 'Safety Rules', 
                    inspection_type = 'Safety', 
                    inspector_name = 'Steven', 
                    start_hour = 10, 
                    start_minute = 0, 
                    location_id = 153252, 
                    mt_location = ["1space"], )
            )
        else:
            return RestV10ProjectsProjectIdInspectionLogsPostRequest(
                inspection_log = procore_sdk.models.rest_v10_projects_project_id_inspection_logs_post_request_inspection_log.RestV10ProjectsProjectIdInspectionLogsPost_request_inspection_log(
                    area = 'Level 5', 
                    comments = 'Inspection took a total of 2 hours', 
                    date = 'Thu May 19 00:00:00 UTC 2016', 
                    datetime = '2016-05-19T12:00Z', 
                    end_hour = 10, 
                    end_minute = 0, 
                    inspecting_entity = 'Safety Rules', 
                    inspection_type = 'Safety', 
                    inspector_name = 'Steven', 
                    start_hour = 10, 
                    start_minute = 0, 
                    location_id = 153252, 
                    mt_location = ["1space"], ),
        )
        """

    def testRestV10ProjectsProjectIdInspectionLogsPostRequest(self):
        """Test RestV10ProjectsProjectIdInspectionLogsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
