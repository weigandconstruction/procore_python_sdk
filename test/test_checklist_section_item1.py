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

from procore_sdk.models.checklist_section_item1 import ChecklistSectionItem1

class TestChecklistSectionItem1(unittest.TestCase):
    """ChecklistSectionItem1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistSectionItem1:
        """Test ChecklistSectionItem1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistSectionItem1`
        """
        model = ChecklistSectionItem1()
        if include_optional:
            return ChecklistSectionItem1(
                id = 2,
                name = 'Item 1',
                details = '+/- 1 degrees',
                status = 'yes',
                responded_with = 'Safe - Knowledge',
                origin_id = 1,
                section_id = 21,
                position = 1,
                observations = [
                    procore_sdk.models.checklist_section_item_1_observations_inner.Checklist_Section_Item_1_observations_inner(
                        id = 2085, 
                        created_at = '2012-10-23T21:39:40Z', 
                        number = '56', 
                        status = 'initiated', 
                        title = 'Clean up paint splatter', 
                        type = procore_sdk.models.checklist_section_item_1_observations_inner_type.Checklist_Section_Item_1_observations_inner_type(
                            id = 4952, 
                            name = 'Deficiency', ), 
                        assignee = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                            id = 160586, 
                            login = 'exampleuser@example.com', 
                            name = 'Carl Contractor', ), 
                        created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                            id = 160586, 
                            login = 'exampleuser@example.com', 
                            name = 'Carl Contractor', ), )
                    ],
                attachment_histories = [
                    procore_sdk.models.checklist_section_item_1_attachment_histories_inner.Checklist_Section_Item_1_attachment_histories_inner(
                        id = 6485, 
                        created_at = '2012-10-23T21:39:40Z', 
                        created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                            id = 160586, 
                            login = 'exampleuser@example.com', 
                            name = 'Carl Contractor', ), 
                        attachment = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                            id = 5324, 
                            url = 'http://www.example.com/', 
                            filename = 'january_receipt_copy.jpg', ), )
                    ],
                attachments = [
                    procore_sdk.models.checklist_section_item_1_attachments_inner.Checklist_Section_Item_1_attachments_inner(
                        id = 34, 
                        url = 'http://www.example.com/test.pdf', 
                        filename = 'test.pdf', )
                    ],
                histories = [
                    procore_sdk.models.checklist_section_item_histories_inner.Checklist_Section_Item_histories_inner(
                        id = 56, 
                        body = 'changed the status to yes', 
                        status = 'yes', 
                        responded_with = 'Safe - Knowledge', 
                        created_at = '2012-10-23T21:39:40Z', 
                        created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                            id = 160586, 
                            login = 'exampleuser@example.com', 
                            name = 'Carl Contractor', ), )
                    ],
                item_response = procore_sdk.models.checklist_item_response.ChecklistItemResponse(
                    item_id = 4323, 
                    status = 'conforming', 
                    responded_at = '2018-10-23T21:39:40Z', 
                    responder = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                        id = 160586, 
                        login = 'exampleuser@example.com', 
                        name = 'Carl Contractor', ), 
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
                            name = 'Safe', ), ), ),
                comments = [
                    procore_sdk.models.checklist_section_item_comments_inner.Checklist_Section_Item_comments_inner(
                        id = 4798, 
                        body = 'Paint splatter is also on the top panel of the frame.', 
                        created_at = '2012-10-23T21:39:40Z', 
                        created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                            id = 160586, 
                            login = 'exampleuser@example.com', 
                            name = 'Carl Contractor', ), )
                    ],
                response = procore_sdk.models.checklist_response.ChecklistResponse(
                    id = 1, 
                    name = 'Safe - Knowledge', 
                    corresponding_status = 'yes', ),
                response_set = procore_sdk.models.checklist_section_item_1_response_set.Checklist_Section_Item_1_response_set(
                    id = 83, 
                    name = 'Safety Responses', 
                    responses = [
                        procore_sdk.models.checklist_response.ChecklistResponse(
                            id = 1, 
                            name = 'Safe - Knowledge', 
                            corresponding_status = 'yes', )
                        ], 
                    created_at = '2012-10-23T21:39:40Z', 
                    updated_at = '2012-10-23T21:39:40Z', ),
                response_set_id = 9,
                type = procore_sdk.models.checklist_item_type.ChecklistItemType(
                    id = 1, 
                    category = 'multiple_choice', 
                    name = 'default', ),
                template_item_id = 3,
                response_type_id = 3,
                updated_at = '2012-10-23T21:39:40Z'
            )
        else:
            return ChecklistSectionItem1(
        )
        """

    def testChecklistSectionItem1(self):
        """Test ChecklistSectionItem1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
