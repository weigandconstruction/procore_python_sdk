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

from procore_sdk.models.rest_v10_projects_project_id_users_id_actions_add_post_request_user import RestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser

class TestRestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser(unittest.TestCase):
    """RestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser:
        """Test RestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser`
        """
        model = RestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser()
        if include_optional:
            return RestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser(
                permission_template_id = 56
            )
        else:
            return RestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser(
        )
        """

    def testRestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser(self):
        """Test RestV10ProjectsProjectIdUsersIdActionsAddPostRequestUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
