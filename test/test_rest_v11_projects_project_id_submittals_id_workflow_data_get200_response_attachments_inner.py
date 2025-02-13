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

from procore_sdk.models.rest_v11_projects_project_id_submittals_id_workflow_data_get200_response_attachments_inner import RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner

class TestRestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner(unittest.TestCase):
    """RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner:
        """Test RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner`
        """
        model = RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner()
        if include_optional:
            return RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner(
                id = 56,
                approver_id = 56,
                approver_marked_up_at = '2020-01-28T16:45:06Z',
                can_carry_forward = True,
                download_url = 'https://...',
                has_failed = True,
                is_originating_attachment = True,
                is_processing = True,
                last_marked_up_at = '2020-01-28T16:45:06Z',
                last_marked_up_by = 'Alvin Weinberg',
                name = 'msr_spec.pdf',
                viewer_type = 'document',
                viewer_url = 'https://...'
            )
        else:
            return RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner(
        )
        """

    def testRestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner(self):
        """Test RestV11ProjectsProjectIdSubmittalsIdWorkflowDataGet200ResponseAttachmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
