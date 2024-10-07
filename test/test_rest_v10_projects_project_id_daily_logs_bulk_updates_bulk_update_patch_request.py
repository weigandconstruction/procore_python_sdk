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

from procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request import RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest

class TestRestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest:
        """Test RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest`
        """
        model = RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest()
        if include_optional:
            return RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest(
                updates = procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates.RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch_request_updates(
                    accident_log = [
                        procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_accident_log_inner.RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch_request_updates_accident_log_inner(
                            id = 123, 
                            status = 'approved', )
                        ], 
                    call_log = [
                        procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_accident_log_inner.RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch_request_updates_accident_log_inner(
                            id = 123, 
                            status = 'approved', )
                        ], 
                    delay_log = [
                        
                        ], 
                    delivery_log = [
                        
                        ], 
                    dumpster_log = [
                        
                        ], 
                    equipment_log = [
                        
                        ], 
                    inspection_log = [
                        
                        ], 
                    manpower_log = [
                        
                        ], 
                    daily_construction_report_log = [
                        
                        ], 
                    notes_log = [
                        
                        ], 
                    plan_revision_log = [
                        
                        ], 
                    productivity_log = [
                        
                        ], 
                    quantity_log = [
                        
                        ], 
                    safety_violation_log = [
                        
                        ], 
                    timecard_entry = [
                        
                        ], 
                    visitor_log = [
                        
                        ], 
                    waste_log = [
                        
                        ], 
                    work_log = [
                        
                        ], )
            )
        else:
            return RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest(
                updates = procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates.RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch_request_updates(
                    accident_log = [
                        procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_accident_log_inner.RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch_request_updates_accident_log_inner(
                            id = 123, 
                            status = 'approved', )
                        ], 
                    call_log = [
                        procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_accident_log_inner.RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch_request_updates_accident_log_inner(
                            id = 123, 
                            status = 'approved', )
                        ], 
                    delay_log = [
                        
                        ], 
                    delivery_log = [
                        
                        ], 
                    dumpster_log = [
                        
                        ], 
                    equipment_log = [
                        
                        ], 
                    inspection_log = [
                        
                        ], 
                    manpower_log = [
                        
                        ], 
                    daily_construction_report_log = [
                        
                        ], 
                    notes_log = [
                        
                        ], 
                    plan_revision_log = [
                        
                        ], 
                    productivity_log = [
                        
                        ], 
                    quantity_log = [
                        
                        ], 
                    safety_violation_log = [
                        
                        ], 
                    timecard_entry = [
                        
                        ], 
                    visitor_log = [
                        
                        ], 
                    waste_log = [
                        
                        ], 
                    work_log = [
                        
                        ], ),
        )
        """

    def testRestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest(self):
        """Test RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
