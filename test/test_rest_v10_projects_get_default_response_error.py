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

from procore_sdk.models.rest_v10_projects_get_default_response_error import RestV10ProjectsGetDefaultResponseError

class TestRestV10ProjectsGetDefaultResponseError(unittest.TestCase):
    """RestV10ProjectsGetDefaultResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsGetDefaultResponseError:
        """Test RestV10ProjectsGetDefaultResponseError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsGetDefaultResponseError`
        """
        model = RestV10ProjectsGetDefaultResponseError()
        if include_optional:
            return RestV10ProjectsGetDefaultResponseError(
                code = '',
                message = '',
                details = [
                    procore_sdk.models.rest_v10_projects_get_default_response_error_details_inner.RestV10ProjectsGet_default_response_error_details_inner(
                        code = '', 
                        message = '', 
                        source = '', )
                    ]
            )
        else:
            return RestV10ProjectsGetDefaultResponseError(
                code = '',
                message = '',
        )
        """

    def testRestV10ProjectsGetDefaultResponseError(self):
        """Test RestV10ProjectsGetDefaultResponseError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
