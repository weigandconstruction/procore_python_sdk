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

from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_id_change_history_get304_response import RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response

class TestRestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response(unittest.TestCase):
    """RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response:
        """Test RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response`
        """
        model = RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response()
        if include_optional:
            return RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response(
                id = 101,
                column = 'assignee_id',
                readable_column = 'Assignee',
                formatted_column = 'Assignee',
                old_value = 'The original title',
                new_value = 'The updated title',
                created_by = None,
                created_at = '2018-05-08T13:21:20Z'
            )
        else:
            return RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response(
        )
        """

    def testRestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response(self):
        """Test RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
