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

from procore_sdk.models.meeting3 import Meeting3

class TestMeeting3(unittest.TestCase):
    """Meeting3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Meeting3:
        """Test Meeting3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Meeting3`
        """
        model = Meeting3()
        if include_optional:
            return Meeting3(
                position = 56,
                title = '',
                location = '',
                minutes = '',
                meeting_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                overview = '',
                occurred = True,
                start_time = '',
                finish_time = '',
                time_zone = '',
                is_private = True,
                conclusion = '',
                is_draft = True,
                drawing_revision_ids = [4,5],
                file_version_ids = [6,7],
                form_ids = [7,8],
                image_ids = [9,10],
                upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"]
            )
        else:
            return Meeting3(
        )
        """

    def testMeeting3(self):
        """Test Meeting3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
