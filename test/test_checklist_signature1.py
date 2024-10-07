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

from procore_sdk.models.checklist_signature1 import ChecklistSignature1

class TestChecklistSignature1(unittest.TestCase):
    """ChecklistSignature1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistSignature1:
        """Test ChecklistSignature1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistSignature1`
        """
        model = ChecklistSignature1()
        if include_optional:
            return ChecklistSignature1(
                id = 5324,
                captured_by = None,
                captured_at = '2012-10-23T21:39:40Z',
                attachment = procore_sdk.models.checklist_signature_1_attachment.Checklist_Signature_1_attachment(
                    id = 5324, 
                    url = 'http://www.example.com/', 
                    filename = 'january_receipt_copy.jpg', 
                    name = 'january_receipt_copy.jpg', )
            )
        else:
            return ChecklistSignature1(
        )
        """

    def testChecklistSignature1(self):
        """Test ChecklistSignature1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
