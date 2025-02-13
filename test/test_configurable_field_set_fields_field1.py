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

from procore_sdk.models.configurable_field_set_fields_field1 import ConfigurableFieldSetFieldsField1

class TestConfigurableFieldSetFieldsField1(unittest.TestCase):
    """ConfigurableFieldSetFieldsField1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurableFieldSetFieldsField1:
        """Test ConfigurableFieldSetFieldsField1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurableFieldSetFieldsField1`
        """
        model = ConfigurableFieldSetFieldsField1()
        if include_optional:
            return ConfigurableFieldSetFieldsField1(
                name = 'field_1',
                visible = True,
                required = True
            )
        else:
            return ConfigurableFieldSetFieldsField1(
        )
        """

    def testConfigurableFieldSetFieldsField1(self):
        """Test ConfigurableFieldSetFieldsField1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
