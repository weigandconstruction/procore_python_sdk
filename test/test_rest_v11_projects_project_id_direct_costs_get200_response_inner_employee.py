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

from procore_sdk.models.rest_v11_projects_project_id_direct_costs_get200_response_inner_employee import RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee

class TestRestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee(unittest.TestCase):
    """RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee:
        """Test RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee`
        """
        model = RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee()
        if include_optional:
            return RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee(
                id = 5,
                name = 'Bob the Builder'
            )
        else:
            return RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee(
        )
        """

    def testRestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee(self):
        """Test RestV11ProjectsProjectIdDirectCostsGet200ResponseInnerEmployee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
