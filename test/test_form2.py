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

from procore_sdk.models.form2 import Form2

class TestForm2(unittest.TestCase):
    """Form2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Form2:
        """Test Form2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Form2`
        """
        model = Form2()
        if include_optional:
            return Form2(
                name = '1',
                description = 'This is a description',
                private = False,
                fillable_pdf_prostore_file_id = 5432,
                prostore_file_ids = [4,5]
            )
        else:
            return Form2(
        )
        """

    def testForm2(self):
        """Test Form2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
