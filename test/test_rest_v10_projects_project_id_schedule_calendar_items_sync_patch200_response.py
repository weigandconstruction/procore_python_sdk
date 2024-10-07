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

from procore_sdk.models.rest_v10_projects_project_id_schedule_calendar_items_sync_patch200_response import RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response

class TestRestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response(unittest.TestCase):
    """RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response:
        """Test RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response`
        """
        model = RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response()
        if include_optional:
            return RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response(
                entities = [
                    procore_sdk.models.rest_v10_projects_project_id_schedule_calendar_items_get_200_response_inner.RestV10ProjectsProjectIdScheduleCalendarItemsGet_200_response_inner(
                        id = 56, 
                        assigned = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                            id = 160586, 
                            login = 'carl.contractor@example.com', 
                            name = 'Carl Contractor', ), 
                        color = '#A4505D', 
                        created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                            id = 160586, 
                            login = 'carl.contractor@example.com', 
                            name = 'Carl Contractor', ), 
                        description = 'Use some power tools to fix the drywall.', 
                        finish = 'Sun Feb 02 00:00:00 UTC 2020', 
                        full_outline_path = 'Fix drywall', 
                        milestone = True, 
                        name = 'Fix Drywall', 
                        percentage = 50, 
                        private = False, 
                        start = 'Wed Jan 01 00:00:00 UTC 2020', 
                        task_name = 'Fix Drywall', 
                        updated_at = '2019-08-01T00:00Z', )
                    ],
                errors = [
                    procore_sdk.models.rest_v10_tax_types_post_400_response.RestV10TaxTypesPost_400_response(
                        errors = procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch_200_response_errors_inner_all_of_errors.RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch_200_response_errors_inner_allOf_errors(
                            field_name = [
                                ''
                                ], ), )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response(
        )
        """

    def testRestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response(self):
        """Test RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
