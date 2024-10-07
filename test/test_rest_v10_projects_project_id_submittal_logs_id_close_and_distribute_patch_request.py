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

from procore_sdk.models.rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request import RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest

class TestRestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest:
        """Test RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest`
        """
        model = RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest()
        if include_optional:
            return RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest(
                submittal_log_status_id = 1,
                submittal_description = 'Submittal Description',
                message = 'Message Content',
                prostore_file_ids = [
                    1
                    ],
                recipient_ids = [
                    1
                    ],
                selected_approvers = [
                    procore_sdk.models.rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request_selected_approvers_inner.RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch_request_selected_approvers_inner(
                        id = 100, 
                        include_comment = True, 
                        attachment_ids = [
                            200
                            ], )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest(
        )
        """

    def testRestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest(self):
        """Test RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
