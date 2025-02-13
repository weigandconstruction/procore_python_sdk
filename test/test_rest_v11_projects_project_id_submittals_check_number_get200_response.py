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

from procore_sdk.models.rest_v11_projects_project_id_submittals_check_number_get200_response import RestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response

class TestRestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response(unittest.TestCase):
    """RestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response:
        """Test RestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response`
        """
        model = RestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response()
        if include_optional:
            return RestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response(
                next_number = '2',
                number_available = True,
                current_number = '100.1'
            )
        else:
            return RestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response(
        )
        """

    def testRestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response(self):
        """Test RestV11ProjectsProjectIdSubmittalsCheckNumberGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
