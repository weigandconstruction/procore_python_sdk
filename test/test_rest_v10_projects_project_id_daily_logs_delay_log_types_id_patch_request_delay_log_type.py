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

from procore_sdk.models.rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch_request_delay_log_type import RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType

class TestRestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType(unittest.TestCase):
    """RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType:
        """Test RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType`
        """
        model = RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType()
        if include_optional:
            return RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType(
                visible = False
            )
        else:
            return RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType(
        )
        """

    def testRestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType(self):
        """Test RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequestDelayLogType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
