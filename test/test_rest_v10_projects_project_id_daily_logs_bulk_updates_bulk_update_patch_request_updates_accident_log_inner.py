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

from procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_accident_log_inner import RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner

class TestRestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner(unittest.TestCase):
    """RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner:
        """Test RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner`
        """
        model = RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner()
        if include_optional:
            return RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner(
                id = 123,
                status = 'approved'
            )
        else:
            return RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner(
                id = 123,
                status = 'approved',
        )
        """

    def testRestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner(self):
        """Test RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
