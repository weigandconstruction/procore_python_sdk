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

from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_post_request_list import RestV10ProjectsProjectIdChecklistListsPostRequestList

class TestRestV10ProjectsProjectIdChecklistListsPostRequestList(unittest.TestCase):
    """RestV10ProjectsProjectIdChecklistListsPostRequestList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdChecklistListsPostRequestList:
        """Test RestV10ProjectsProjectIdChecklistListsPostRequestList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdChecklistListsPostRequestList`
        """
        model = RestV10ProjectsProjectIdChecklistListsPostRequestList()
        if include_optional:
            return RestV10ProjectsProjectIdChecklistListsPostRequestList(
                description = 'Ensure proper window installation',
                due_at = '2019-08-18T23:36:30Z',
                inspection_date = 'Thu Oct 31 00:00:00 UTC 2019',
                inspection_type_id = 34,
                number = 42,
                managed_equipment_id = 123,
                point_of_contact_id = 12,
                inspector_ids = [12,13],
                private = True,
                responsible_contractor_id = 123,
                spec_section_id = 5,
                status = 'open',
                trade_id = 123,
                distribution_member_ids = [2,3],
                location_id = 1,
                custom_field_custom_field_definition_id = custom field value
            )
        else:
            return RestV10ProjectsProjectIdChecklistListsPostRequestList(
        )
        """

    def testRestV10ProjectsProjectIdChecklistListsPostRequestList(self):
        """Test RestV10ProjectsProjectIdChecklistListsPostRequestList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
