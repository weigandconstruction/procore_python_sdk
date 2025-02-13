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

from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response_meeting_categories_inner import RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner

class TestRestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner(unittest.TestCase):
    """RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner:
        """Test RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner`
        """
        model = RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner()
        if include_optional:
            return RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner(
                id = 192424,
                title = 'Uncategorized Items',
                position = 0,
                meeting_topic = [
                    procore_sdk.models.rest_v11_projects_project_id_meetings_post_201_response_meeting_categories_inner_meeting_topic_inner.RestV11ProjectsProjectIdMeetingsPost_201_response_meeting_categories_inner_meeting_topic_inner(
                        id = 965039, 
                        number = '1.1', 
                        created_on = 'Fri Apr 25 00:00:00 UTC 2014', 
                        position = 0, 
                        due_date = 'Tue May 20 00:00:00 UTC 2014', 
                        priority = 'Low', 
                        status = 'On Hold', 
                        title = '34' Level', 
                        minutes = '<p><span style=\"font-size: large;\">Please look at Item 1 and have those pieces completed <strong>before</strong></span></p>', 
                        description = 'Need pricing from vendor for 34' level', 
                        meeting_category = procore_sdk.models.rest_v11_projects_project_id_meetings_post_201_response_meeting_categories_inner_meeting_topic_inner_meeting_category.RestV11ProjectsProjectIdMeetingsPost_201_response_meeting_categories_inner_meeting_topic_inner_meeting_category(
                            id = 192424, 
                            title = 'Uncategorized Items', ), 
                        assignments = [
                            procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                                id = 160586, 
                                login = 'carl.contractor@example.com', 
                                name = 'Carl Contractor', )
                            ], 
                        attachments = [
                            procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                                id = 5324, 
                                url = 'http://www.example.com/', 
                                filename = 'january_receipt_copy.jpg', )
                            ], 
                        download_all_url = 'http://localhost:3000/1/company/attachments/download_all?uuid=9ab95907a82318e6403c0896bde48ad9e29f', )
                    ]
            )
        else:
            return RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner(
        )
        """

    def testRestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner(self):
        """Test RestV11ProjectsProjectIdMeetingsPost201ResponseMeetingCategoriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
