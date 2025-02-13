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

from procore_sdk.models.rest_v10_projects_project_id_daily_logs_clones_post201_response import RestV10ProjectsProjectIdDailyLogsClonesPost201Response

class TestRestV10ProjectsProjectIdDailyLogsClonesPost201Response(unittest.TestCase):
    """RestV10ProjectsProjectIdDailyLogsClonesPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDailyLogsClonesPost201Response:
        """Test RestV10ProjectsProjectIdDailyLogsClonesPost201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDailyLogsClonesPost201Response`
        """
        model = RestV10ProjectsProjectIdDailyLogsClonesPost201Response()
        if include_optional:
            return RestV10ProjectsProjectIdDailyLogsClonesPost201Response(
                notes_log = procore_sdk.models.rest_v10_projects_project_id_daily_logs_clones_post_201_response_notes_log.RestV10ProjectsProjectIdDailyLogsClonesPost_201_response_notes_log(
                    id = 9, 
                    comment = '123', 
                    created_at = '2021-01-07T21:37:43Z', 
                    created_by_collaborator = True, 
                    custom_fields = procore_sdk.models.custom_fields.custom_fields(), 
                    date = 'Thu Jan 07 00:00:00 UTC 2021', 
                    datetime = '2021-01-07T20:00Z', 
                    daily_log_header_id = 4, 
                    deleted_at = '', 
                    is_issue_day = '', 
                    permissions = procore_sdk.models.rest_v10_projects_project_id_daily_logs_clones_post_201_response_notes_log_permissions.RestV10ProjectsProjectIdDailyLogsClonesPost_201_response_notes_log_permissions(
                        can_update = True, 
                        can_delete = True, ), 
                    position = 9, 
                    updated_at = '2021-01-07T21:37:43Z', 
                    status = 'approved', 
                    attachments = [
                        None
                        ], 
                    created_by = procore_sdk.models.rest_v10_projects_project_id_daily_logs_clones_post_201_response_notes_log_created_by.RestV10ProjectsProjectIdDailyLogsClonesPost_201_response_notes_log_created_by(
                        id = 3, 
                        login = 'carl.contractor@example.com', 
                        name = '', ), 
                    location = '', )
            )
        else:
            return RestV10ProjectsProjectIdDailyLogsClonesPost201Response(
        )
        """

    def testRestV10ProjectsProjectIdDailyLogsClonesPost201Response(self):
        """Test RestV10ProjectsProjectIdDailyLogsClonesPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
