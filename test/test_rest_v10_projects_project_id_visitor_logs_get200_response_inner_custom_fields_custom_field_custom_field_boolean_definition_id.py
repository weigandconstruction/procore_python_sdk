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

from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner_custom_fields_custom_field_custom_field_boolean_definition_id import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId

class TestRestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId(unittest.TestCase):
    """RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId:
        """Test RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId`
        """
        model = RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId()
        if include_optional:
            return RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId(
                data_type = 'boolean',
                value = True
            )
        else:
            return RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId(
        )
        """

    def testRestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId(self):
        """Test RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFieldsCustomFieldCustomFieldBooleanDefinitionId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
