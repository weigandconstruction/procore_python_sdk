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

from procore_sdk.models.project_region3 import ProjectRegion3

class TestProjectRegion3(unittest.TestCase):
    """ProjectRegion3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectRegion3:
        """Test ProjectRegion3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectRegion3`
        """
        model = ProjectRegion3()
        if include_optional:
            return ProjectRegion3(
                name = 'NW'
            )
        else:
            return ProjectRegion3(
        )
        """

    def testProjectRegion3(self):
        """Test ProjectRegion3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
