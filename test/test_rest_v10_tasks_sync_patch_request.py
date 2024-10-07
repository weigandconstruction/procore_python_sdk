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

from procore_sdk.models.rest_v10_tasks_sync_patch_request import RestV10TasksSyncPatchRequest

class TestRestV10TasksSyncPatchRequest(unittest.TestCase):
    """RestV10TasksSyncPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10TasksSyncPatchRequest:
        """Test RestV10TasksSyncPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10TasksSyncPatchRequest`
        """
        model = RestV10TasksSyncPatchRequest()
        if include_optional:
            return RestV10TasksSyncPatchRequest(
                project_id = 101429,
                updates = [
                    procore_sdk.models.rest_v10_tasks_sync_patch_request_updates_inner.RestV10TasksSyncPatch_request_updates_inner(
                        name = 'INTERIOR', 
                        start = '2015-03-06T13:00Z', 
                        finish = '2015-03-08T22:00Z', 
                        actual_start = '2015-03-08T00:00Z', 
                        actual_finish = '2015-03-09T00:00Z', 
                        percentage = 80, 
                        critical_path = False, 
                        milestone = False, 
                        row_number = 2, 
                        has_children = False, 
                        source_uid = '0687b2f6-dc92-40c7-a8c8-a3c1f3ac9305', 
                        parent_id = 802241, 
                        full_outline_path = 'INTERIOR', 
                        activity_id = 'EM12865', 
                        wbs = '1.1', 
                        schedule_duration = 3, 
                        resource_ids = [1,2,3], 
                        notes = 'Some notes', 
                        baseline_start = '2015-03-08T00:00Z', 
                        baseline_finish = '2015-03-09T00:00Z', 
                        start_variance = 1.5, 
                        finish_variance = -2.5, 
                        manually_edited = False, )
                    ]
            )
        else:
            return RestV10TasksSyncPatchRequest(
                project_id = 101429,
                updates = [
                    procore_sdk.models.rest_v10_tasks_sync_patch_request_updates_inner.RestV10TasksSyncPatch_request_updates_inner(
                        name = 'INTERIOR', 
                        start = '2015-03-06T13:00Z', 
                        finish = '2015-03-08T22:00Z', 
                        actual_start = '2015-03-08T00:00Z', 
                        actual_finish = '2015-03-09T00:00Z', 
                        percentage = 80, 
                        critical_path = False, 
                        milestone = False, 
                        row_number = 2, 
                        has_children = False, 
                        source_uid = '0687b2f6-dc92-40c7-a8c8-a3c1f3ac9305', 
                        parent_id = 802241, 
                        full_outline_path = 'INTERIOR', 
                        activity_id = 'EM12865', 
                        wbs = '1.1', 
                        schedule_duration = 3, 
                        resource_ids = [1,2,3], 
                        notes = 'Some notes', 
                        baseline_start = '2015-03-08T00:00Z', 
                        baseline_finish = '2015-03-09T00:00Z', 
                        start_variance = 1.5, 
                        finish_variance = -2.5, 
                        manually_edited = False, )
                    ],
        )
        """

    def testRestV10TasksSyncPatchRequest(self):
        """Test RestV10TasksSyncPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
