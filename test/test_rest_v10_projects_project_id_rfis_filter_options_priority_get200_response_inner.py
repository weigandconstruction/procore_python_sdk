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

from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_priority_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner

class TestRestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner:
        """Test RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner(
                key = 1,
                value = 'Medium'
            )
        else:
            return RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
