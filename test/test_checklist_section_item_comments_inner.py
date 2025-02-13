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

from procore_sdk.models.checklist_section_item_comments_inner import ChecklistSectionItemCommentsInner

class TestChecklistSectionItemCommentsInner(unittest.TestCase):
    """ChecklistSectionItemCommentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistSectionItemCommentsInner:
        """Test ChecklistSectionItemCommentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistSectionItemCommentsInner`
        """
        model = ChecklistSectionItemCommentsInner()
        if include_optional:
            return ChecklistSectionItemCommentsInner(
                id = 4798,
                body = 'Paint splatter is also on the top panel of the frame.',
                created_at = '2012-10-23T21:39:40Z',
                created_by = procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post_201_response_all_of_created_by.RestV10ProjectsProjectIdChecklistListTemplatesPost_201_response_allOf_created_by(
                    id = 160586, 
                    login = 'exampleuser@example.com', 
                    name = 'Carl Contractor', )
            )
        else:
            return ChecklistSectionItemCommentsInner(
        )
        """

    def testChecklistSectionItemCommentsInner(self):
        """Test ChecklistSectionItemCommentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
