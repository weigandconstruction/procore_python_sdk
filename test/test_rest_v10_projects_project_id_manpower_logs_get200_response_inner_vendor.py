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

from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get200_response_inner_vendor import RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor

class TestRestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor(unittest.TestCase):
    """RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor:
        """Test RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor`
        """
        model = RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor()
        if include_optional:
            return RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor(
                id = 324,
                name = 'AAA Constructions'
            )
        else:
            return RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor(
        )
        """

    def testRestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor(self):
        """Test RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerVendor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
