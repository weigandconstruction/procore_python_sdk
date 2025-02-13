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

from procore_sdk.models.rfi_body1_rfi_question import RFIBody1RfiQuestion

class TestRFIBody1RfiQuestion(unittest.TestCase):
    """RFIBody1RfiQuestion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RFIBody1RfiQuestion:
        """Test RFIBody1RfiQuestion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RFIBody1RfiQuestion`
        """
        model = RFIBody1RfiQuestion()
        if include_optional:
            return RFIBody1RfiQuestion(
                body = 'What color should the kitchen wall be?',
                attachments = ["Content-Type: text/plain\\nContent of a.txt.\\n","Content-Type: text/html\\n<!DOCTYPE html><title>Content of a.html.</title>\\n"],
                drawing_revision_ids = [4,5],
                file_version_ids = [6,7],
                form_ids = [7,8],
                image_ids = [9,10],
                upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"]
            )
        else:
            return RFIBody1RfiQuestion(
                body = 'What color should the kitchen wall be?',
        )
        """

    def testRFIBody1RfiQuestion(self):
        """Test RFIBody1RfiQuestion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
