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

from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete400_response import RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response

class TestRestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response(unittest.TestCase):
    """RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response:
        """Test RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response`
        """
        model = RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response()
        if include_optional:
            return RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response(
                code = 56,
                message = '',
                fields = '',
                reason = '',
                error = procore_sdk.models.rest_v10_company_configuration_get_400_response_error.RestV10CompanyConfigurationGet_400_response_error(
                    code = 'BAD_REQUEST', 
                    message = 'Missing Project or Company ID', )
            )
        else:
            return RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response(
        )
        """

    def testRestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response(self):
        """Test RestV10ProjectsProjectIdChecklistSchedulesScheduleIdAttachmentsIdDelete400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
