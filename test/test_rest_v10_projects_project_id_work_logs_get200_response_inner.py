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

from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner import RestV10ProjectsProjectIdWorkLogsGet200ResponseInner

class TestRestV10ProjectsProjectIdWorkLogsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdWorkLogsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdWorkLogsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdWorkLogsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdWorkLogsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdWorkLogsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdWorkLogsGet200ResponseInner(
                id = 333675,
                comments = 'Work Log Comments',
                created_at = '2012-10-23T21:39:40Z',
                var_date = 'Thu May 19 00:00:00 UTC 2016',
                datetime = '2016-05-19T12:00Z',
                deleted_at = '2017-07-29T21:39:40Z',
                hourly_rate = 20,
                hours = 12,
                position = 142143,
                reimbursable = True,
                resource_name = 'Alices Admin (Twenty Twelve Inc)',
                showed = True,
                workers = 6,
                updated_at = '2012-10-24T21:39:40Z',
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                attachments = [
                    procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get_200_response_inner_attachments_inner.RestV10CompaniesCompanyIdWorkflowPermanentLogsGet_200_response_inner_attachments_inner(
                        id = 56, 
                        name = '', 
                        url = '', 
                        filename = '', )
                    ],
                scheduled_tasks = [
                    procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_scheduled_tasks_inner.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_scheduled_tasks_inner(
                        id = 100884, 
                        work_log_id = 28652, 
                        task_name = 'Concrete Pre-Pour', 
                        task_percentage = 50, 
                        task_id = 198325, 
                        task_row_number = 987654, )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdWorkLogsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdWorkLogsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdWorkLogsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
