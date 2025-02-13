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

from procore_sdk.models.rest_v10_projects_project_id_timesheets_update_approval_patch_request import RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest

class TestRestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest:
        """Test RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest`
        """
        model = RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest()
        if include_optional:
            return RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest(
                timesheets = [
                    procore_sdk.models.rest_v10_projects_project_id_timesheets_update_approval_patch_request_timesheets_inner.RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatch_request_timesheets_inner(
                        id = 1, 
                        status = 'approved', )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest(
                timesheets = [
                    procore_sdk.models.rest_v10_projects_project_id_timesheets_update_approval_patch_request_timesheets_inner.RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatch_request_timesheets_inner(
                        id = 1, 
                        status = 'approved', )
                    ],
        )
        """

    def testRestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest(self):
        """Test RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
