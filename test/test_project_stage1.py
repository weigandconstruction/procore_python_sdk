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

from procore_sdk.models.project_stage1 import ProjectStage1

class TestProjectStage1(unittest.TestCase):
    """ProjectStage1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectStage1:
        """Test ProjectStage1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectStage1`
        """
        model = ProjectStage1()
        if include_optional:
            return ProjectStage1(
                id = 3,
                name = 'Course of Construction'
            )
        else:
            return ProjectStage1(
        )
        """

    def testProjectStage1(self):
        """Test ProjectStage1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
