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

from procore_sdk.models.rest_v10_projects_project_id_drawing_sets_post_request import RestV10ProjectsProjectIdDrawingSetsPostRequest

class TestRestV10ProjectsProjectIdDrawingSetsPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdDrawingSetsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDrawingSetsPostRequest:
        """Test RestV10ProjectsProjectIdDrawingSetsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDrawingSetsPostRequest`
        """
        model = RestV10ProjectsProjectIdDrawingSetsPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdDrawingSetsPostRequest(
                name = 'another new drawing set',
                var_date = 'Wed Aug 31 00:00:00 UTC 2016'
            )
        else:
            return RestV10ProjectsProjectIdDrawingSetsPostRequest(
                name = 'another new drawing set',
        )
        """

    def testRestV10ProjectsProjectIdDrawingSetsPostRequest(self):
        """Test RestV10ProjectsProjectIdDrawingSetsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
