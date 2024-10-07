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

from procore_sdk.models.array_of_tasks_errors_inner import ArrayOfTasksErrorsInner

class TestArrayOfTasksErrorsInner(unittest.TestCase):
    """ArrayOfTasksErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayOfTasksErrorsInner:
        """Test ArrayOfTasksErrorsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayOfTasksErrorsInner`
        """
        model = ArrayOfTasksErrorsInner()
        if include_optional:
            return ArrayOfTasksErrorsInner(
                id = 1359235,
                name = 'INTERIOR',
                task_name = 'INTERIOR',
                key = '101429|40e65ab5-07a5-4cb3-88c0-bc691c3902e0',
                start_datetime = '2015-03-06T13:00Z',
                finish_datetime = '2015-03-08T22:00Z',
                percentage = 80,
                color = '#6070A0',
                parent_id = 802241,
                pending = False,
                activity_id = '0687b2f6-dc92-40c7-a8c8-a3c1f3ac9305',
                schedule_activity_id = 'EM12865',
                resource_name = 'Resource 1, Resource 2, Resource 3',
                critical_path = False,
                milestone = False,
                actual_start = '2015-03-08T00:00Z',
                actual_finish = '2015-03-09T00:00Z',
                row_number = 2,
                has_children = False,
                full_outline_path = 'INTERIOR',
                source_uid = '0687b2f6-dc92-40c7-a8c8-a3c1f3ac9305',
                wbs = '1.1',
                schedule_duration = 3,
                resource_ids = [1,2,3],
                notes = 'Some notes',
                baseline_start = '2015-03-08T00:00Z',
                baseline_finish = '2015-03-09T00:00Z',
                start_variance = 1.5,
                finish_variance = -2.5,
                manually_edited = False,
                created_at = '2015-03-05T11:00Z',
                updated_at = '2015-03-06T13:00Z',
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                updated_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                errors = procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch_200_response_errors_inner_all_of_errors.RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch_200_response_errors_inner_allOf_errors(
                    field_name = [
                        ''
                        ], )
            )
        else:
            return ArrayOfTasksErrorsInner(
        )
        """

    def testArrayOfTasksErrorsInner(self):
        """Test ArrayOfTasksErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
