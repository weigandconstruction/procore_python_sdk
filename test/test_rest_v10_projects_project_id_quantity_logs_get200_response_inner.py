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

from procore_sdk.models.rest_v10_projects_project_id_quantity_logs_get200_response_inner import RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner

class TestRestV10ProjectsProjectIdQuantityLogsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner(
                id = 333675,
                created_at = '2012-10-23T21:39:40Z',
                var_date = 'Thu May 19 00:00:00 UTC 2016',
                datetime = '2016-05-19T12:00Z',
                deleted_at = '2017-07-29T21:39:40Z',
                description = 'Quantity amount was exact',
                position = 11241,
                quantity = 4,
                unit = '5',
                updated_at = '2012-10-24T21:39:40Z',
                cost_code = procore_sdk.models.timecard_entry_full_cost_code.TimecardEntry_full_cost_code(
                    id = 12345, 
                    name = 'Earthwork', ),
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                location = procore_sdk.models.location.Location(
                    id = 15504, 
                    name = '1space>1 space', 
                    node_name = '1 space', 
                    parent_id = 788866, 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', ),
                attachments = [
                    procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get_200_response_inner_attachments_inner.RestV10CompaniesCompanyIdWorkflowPermanentLogsGet_200_response_inner_attachments_inner(
                        id = 56, 
                        name = '', 
                        url = '', 
                        filename = '', )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdQuantityLogsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
