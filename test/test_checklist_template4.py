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

from procore_sdk.models.checklist_template4 import ChecklistTemplate4

class TestChecklistTemplate4(unittest.TestCase):
    """ChecklistTemplate4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistTemplate4:
        """Test ChecklistTemplate4
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistTemplate4`
        """
        model = ChecklistTemplate4()
        if include_optional:
            return ChecklistTemplate4(
                id = 142,
                name = 'Window Inspection',
                description = 'Checklist for circular windows',
                company_description = 'Checklist for windows',
                created_at = '2014-12-10T23:36:30Z',
                updated_at = '2014-12-11T04:58:42Z',
                inspection_type = procore_sdk.models.checklist_template_4_inspection_type.Checklist_Template_4_inspection_type(
                    id = 1, 
                    name = 'Quality', 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', ),
                alternative_response_set_id = 1234,
                response_set = procore_sdk.models.checklist_default_response_set.ChecklistDefaultResponseSet(
                    conforming_response = 'Pass', 
                    deficient_response = 'Fail', 
                    global = True, ),
                location = procore_sdk.models.checklist_template_4_location.Checklist_Template_4_location(
                    id = 15504, 
                    name = '1space>1 space', 
                    node_name = '1 space', 
                    parent_id = 788866, 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', ),
                trade = procore_sdk.models.trade.Trade(
                    id = 999, 
                    name = '09 - acoustical panels', 
                    active = True, 
                    updated_at = '2016-08-01T23:33:54Z', ),
                created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                    id = 160586, 
                    login = 'exampleuser@example.com', 
                    name = 'Carl Contractor', ),
                attachments = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        filename = 'january_receipt_copy.jpg', )
                    ],
                sections = [
                    procore_sdk.models.checklist_template_4_sections_inner.Checklist_Template_4_sections_inner(
                        id = 21, 
                        name = 'Framing', 
                        position = 1, 
                        items = [
                            procore_sdk.models.checklist_template_4_sections_inner_items_inner.Checklist_Template_4_sections_inner_items_inner(
                                id = 2, 
                                name = 'Framing has no visible defects', 
                                status = 'n/a', 
                                section_id = 21, 
                                section_position = 3, 
                                position = 1, )
                            ], )
                    ]
            )
        else:
            return ChecklistTemplate4(
        )
        """

    def testChecklistTemplate4(self):
        """Test ChecklistTemplate4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
