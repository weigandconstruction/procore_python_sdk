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

from procore_sdk.models.project_trigger1 import ProjectTrigger1

class TestProjectTrigger1(unittest.TestCase):
    """ProjectTrigger1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectTrigger1:
        """Test ProjectTrigger1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectTrigger1`
        """
        model = ProjectTrigger1()
        if include_optional:
            return ProjectTrigger1(
                project_id = 23498237,
                api_version = 'v2',
                triggers = [
                    procore_sdk.models.company_trigger_trigger.company_trigger_trigger(
                        resource_name = 'Project Users', 
                        event_type = 'delete', )
                    ]
            )
        else:
            return ProjectTrigger1(
                project_id = 23498237,
                api_version = 'v2',
                triggers = [
                    procore_sdk.models.company_trigger_trigger.company_trigger_trigger(
                        resource_name = 'Project Users', 
                        event_type = 'delete', )
                    ],
        )
        """

    def testProjectTrigger1(self):
        """Test ProjectTrigger1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
