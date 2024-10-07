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

from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_post_request_visitor_log import RestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog

class TestRestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog(unittest.TestCase):
    """RestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog:
        """Test RestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog`
        """
        model = RestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog()
        if include_optional:
            return RestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog(
                begin_hour = 12,
                begin_minute = 10,
                var_date = 'Thu May 19 00:00:00 UTC 2016',
                datetime = '2016-05-19T12:00Z',
                details = 'Visitor Log',
                end_hour = 14,
                end_minute = 30,
                custom_field_custom_field_definition_id = custom field value
            )
        else:
            return RestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog(
                begin_hour = 12,
                begin_minute = 10,
                end_hour = 14,
                end_minute = 30,
        )
        """

    def testRestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog(self):
        """Test RestV10ProjectsProjectIdVisitorLogsPostRequestVisitorLog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
