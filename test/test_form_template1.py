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

from procore_sdk.models.form_template1 import FormTemplate1

class TestFormTemplate1(unittest.TestCase):
    """FormTemplate1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FormTemplate1:
        """Test FormTemplate1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormTemplate1`
        """
        model = FormTemplate1()
        if include_optional:
            return FormTemplate1(
                name = 'JHA',
                description = 'Please fill out to the best of your ability',
                fillable_pdf = ''
            )
        else:
            return FormTemplate1(
        )
        """

    def testFormTemplate1(self):
        """Test FormTemplate1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
