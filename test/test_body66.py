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

from procore_sdk.models.body66 import Body66

class TestBody66(unittest.TestCase):
    """Body66 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body66:
        """Test Body66
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body66`
        """
        model = Body66()
        if include_optional:
            return Body66(
                project_id = 56,
                meeting_id = 56,
                meeting_topic = procore_sdk.models.meeting_topic.Meeting Topic(
                    title = '', 
                    description = 'Need pricing from vendor for 34' level', 
                    due_date = 'Tue May 20 00:00:00 UTC 2014', 
                    status = 'On Hold', 
                    minutes = '', 
                    is_private = True, 
                    closed_at = '2021-05-20T12:00Z', 
                    priority = 'Low', 
                    added_under_agenda = True, 
                    meeting_wide_number = 56, 
                    meeting_category_id = 192424, 
                    assignment_ids = [
                        160586
                        ], ),
                attachments = [
                    ''
                    ]
            )
        else:
            return Body66(
                project_id = 56,
                meeting_id = 56,
                meeting_topic = procore_sdk.models.meeting_topic.Meeting Topic(
                    title = '', 
                    description = 'Need pricing from vendor for 34' level', 
                    due_date = 'Tue May 20 00:00:00 UTC 2014', 
                    status = 'On Hold', 
                    minutes = '', 
                    is_private = True, 
                    closed_at = '2021-05-20T12:00Z', 
                    priority = 'Low', 
                    added_under_agenda = True, 
                    meeting_wide_number = 56, 
                    meeting_category_id = 192424, 
                    assignment_ids = [
                        160586
                        ], ),
        )
        """

    def testBody66(self):
        """Test Body66"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
