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

from procore_sdk.models.rest_v10_projects_project_id_safety_violation_logs_id_patch_request import RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest

class TestRestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest:
        """Test RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest`
        """
        model = RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest()
        if include_optional:
            return RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest(
                safety_violation_log = procore_sdk.models.rest_v10_projects_project_id_safety_violation_logs_id_patch_request_safety_violation_log.RestV10ProjectsProjectIdSafetyViolationLogsIdPatch_request_safety_violation_log(
                    comments = 'No safety violations', 
                    compliance_due = 'Mon Jun 20 00:00:00 UTC 2016', 
                    issued_to = 'ACL Industries', 
                    safety_notice = 'Safety Notice', 
                    subject = 'hard hats', 
                    time_hour = 12, 
                    time_minute = 15, 
                    date = 'Thu May 19 00:00:00 UTC 2016', 
                    datetime = '2016-05-19T12:00Z', )
            )
        else:
            return RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest(
                safety_violation_log = procore_sdk.models.rest_v10_projects_project_id_safety_violation_logs_id_patch_request_safety_violation_log.RestV10ProjectsProjectIdSafetyViolationLogsIdPatch_request_safety_violation_log(
                    comments = 'No safety violations', 
                    compliance_due = 'Mon Jun 20 00:00:00 UTC 2016', 
                    issued_to = 'ACL Industries', 
                    safety_notice = 'Safety Notice', 
                    subject = 'hard hats', 
                    time_hour = 12, 
                    time_minute = 15, 
                    date = 'Thu May 19 00:00:00 UTC 2016', 
                    datetime = '2016-05-19T12:00Z', ),
        )
        """

    def testRestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest(self):
        """Test RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
