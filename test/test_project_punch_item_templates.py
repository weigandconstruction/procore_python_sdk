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

from procore_sdk.models.project_punch_item_templates import ProjectPunchItemTemplates

class TestProjectPunchItemTemplates(unittest.TestCase):
    """ProjectPunchItemTemplates unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectPunchItemTemplates:
        """Test ProjectPunchItemTemplates
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectPunchItemTemplates`
        """
        model = ProjectPunchItemTemplates()
        if include_optional:
            return ProjectPunchItemTemplates(
                id = 1738,
                active = True,
                company_punch_item_template_id = 4325,
                name = '',
                project_id = 33,
                updated_at = '2012-10-24T21:39:40Z',
                punch_item_manager = procore_sdk.models.punch_item_6_created_by.Punch_Item_6_created_by(
                    id = 1738090, 
                    name = 'John Doe', 
                    login = 'johndoe@example.com', ),
                final_approver = procore_sdk.models.punch_item_6_created_by.Punch_Item_6_created_by(
                    id = 1738090, 
                    name = 'John Doe', 
                    login = 'johndoe@example.com', ),
                template_category = procore_sdk.models.template_category.Template Category(
                    id = 967, 
                    name = '03 - Concrete', ),
                assignee = procore_sdk.models.punch_item_6_created_by.Punch_Item_6_created_by(
                    id = 1738090, 
                    name = 'John Doe', 
                    login = 'johndoe@example.com', ),
                trade = procore_sdk.models.trade.Trade(
                    id = 999, 
                    name = '09 - acoustical panels', 
                    active = True, 
                    updated_at = '2016-08-01T23:33:54Z', )
            )
        else:
            return ProjectPunchItemTemplates(
        )
        """

    def testProjectPunchItemTemplates(self):
        """Test ProjectPunchItemTemplates"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
