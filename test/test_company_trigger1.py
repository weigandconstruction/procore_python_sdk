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

from procore_sdk.models.company_trigger1 import CompanyTrigger1

class TestCompanyTrigger1(unittest.TestCase):
    """CompanyTrigger1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyTrigger1:
        """Test CompanyTrigger1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyTrigger1`
        """
        model = CompanyTrigger1()
        if include_optional:
            return CompanyTrigger1(
                company_id = 5358233,
                api_version = 'v2',
                triggers = [
                    procore_sdk.models.company_trigger_trigger.company_trigger_trigger(
                        resource_name = 'Project Users', 
                        event_type = 'delete', )
                    ]
            )
        else:
            return CompanyTrigger1(
                company_id = 5358233,
                api_version = 'v2',
                triggers = [
                    procore_sdk.models.company_trigger_trigger.company_trigger_trigger(
                        resource_name = 'Project Users', 
                        event_type = 'delete', )
                    ],
        )
        """

    def testCompanyTrigger1(self):
        """Test CompanyTrigger1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
