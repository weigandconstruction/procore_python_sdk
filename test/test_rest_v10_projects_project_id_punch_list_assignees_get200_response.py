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

from procore_sdk.models.rest_v10_projects_project_id_punch_list_assignees_get200_response import RestV10ProjectsProjectIdPunchListAssigneesGet200Response

class TestRestV10ProjectsProjectIdPunchListAssigneesGet200Response(unittest.TestCase):
    """RestV10ProjectsProjectIdPunchListAssigneesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdPunchListAssigneesGet200Response:
        """Test RestV10ProjectsProjectIdPunchListAssigneesGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdPunchListAssigneesGet200Response`
        """
        model = RestV10ProjectsProjectIdPunchListAssigneesGet200Response()
        if include_optional:
            return RestV10ProjectsProjectIdPunchListAssigneesGet200Response(
                id = 54,
                name = 'Name'
            )
        else:
            return RestV10ProjectsProjectIdPunchListAssigneesGet200Response(
        )
        """

    def testRestV10ProjectsProjectIdPunchListAssigneesGet200Response(self):
        """Test RestV10ProjectsProjectIdPunchListAssigneesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
