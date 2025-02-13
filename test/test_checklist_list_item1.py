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

from procore_sdk.models.checklist_list_item1 import ChecklistListItem1

class TestChecklistListItem1(unittest.TestCase):
    """ChecklistListItem1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistListItem1:
        """Test ChecklistListItem1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistListItem1`
        """
        model = ChecklistListItem1()
        if include_optional:
            return ChecklistListItem1(
                id = 2,
                details = '+/- 1 degrees',
                item_response = procore_sdk.models.checklist_item_response.ChecklistItemResponse(
                    item_id = 4323, 
                    item_type = procore_sdk.models.checklist_item_type.ChecklistItemType(
                        id = 1, 
                        category = 'multiple_choice', 
                        name = 'default', ), 
                    payload = procore_sdk.models.checklist_item_response_payload.ChecklistItemResponse_payload(
                        text_value = 'Supplies arrived at 10:00 AM', 
                        number_value = 4232, 
                        date_value = 'Sun Jan 20 00:00:00 UTC 2019', 
                        response_option = procore_sdk.models.checklist_item_response_payload_response_option.ChecklistItemResponse_payload_response_option(
                            id = 3432, 
                            name = 'Safe', ), ), 
                    responded_at = '2018-10-23T21:39:40Z', 
                    responder = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                        id = 160586, 
                        login = 'exampleuser@example.com', 
                        name = 'Carl Contractor', ), 
                    status = 'conforming', ),
                list_id = 1,
                name = 'Item 1',
                position = 1,
                responded_with = 'Safe - Knowledge',
                response = procore_sdk.models.checklist_response.ChecklistResponse(
                    id = 1, 
                    name = 'Safe - Knowledge', 
                    corresponding_status = 'yes', ),
                response_set = procore_sdk.models.checklist_list_item_1_response_set.Checklist_List_Item_1_response_set(
                    id = 83, 
                    name = 'Safety Responses', 
                    responses = [
                        procore_sdk.models.checklist_response.ChecklistResponse(
                            id = 1, 
                            name = 'Safe - Knowledge', 
                            corresponding_status = 'yes', 
                            item_status_id = 1, )
                        ], 
                    created_at = '2012-10-23T21:39:40Z', 
                    updated_at = '2012-10-23T21:39:40Z', ),
                response_type_id = 9,
                section_id = 21,
                status = 'yes',
                template_item_id = 3,
                type = procore_sdk.models.checklist_item_type.ChecklistItemType(
                    id = 1, 
                    category = 'multiple_choice', 
                    name = 'default', ),
                updated_at = '2012-10-23T21:39:40Z'
            )
        else:
            return ChecklistListItem1(
        )
        """

    def testChecklistListItem1(self):
        """Test ChecklistListItem1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
