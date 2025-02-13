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

from procore_sdk.models.rest_v10_projects_project_id_plan_revision_logs_post_request_plan_revision_log import RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog

class TestRestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog(unittest.TestCase):
    """RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog:
        """Test RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog`
        """
        model = RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog()
        if include_optional:
            return RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog(
                category = 'Plan Revision Category',
                comments = 'Plan Revision comments',
                var_date = 'Thu May 19 00:00:00 UTC 2016',
                plan_number = '3plan#',
                revision = '763892',
                title = 'Plan Revision title'
            )
        else:
            return RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog(
        )
        """

    def testRestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog(self):
        """Test RestV10ProjectsProjectIdPlanRevisionLogsPostRequestPlanRevisionLog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
