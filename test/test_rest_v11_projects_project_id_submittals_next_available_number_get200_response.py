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

from procore_sdk.models.rest_v11_projects_project_id_submittals_next_available_number_get200_response import RestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response

class TestRestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response(unittest.TestCase):
    """RestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response:
        """Test RestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response`
        """
        model = RestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response()
        if include_optional:
            return RestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response(
                next_number = '2'
            )
        else:
            return RestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response(
        )
        """

    def testRestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response(self):
        """Test RestV11ProjectsProjectIdSubmittalsNextAvailableNumberGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
