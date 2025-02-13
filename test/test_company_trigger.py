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

from procore_sdk.models.company_trigger import CompanyTrigger

class TestCompanyTrigger(unittest.TestCase):
    """CompanyTrigger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyTrigger:
        """Test CompanyTrigger
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyTrigger`
        """
        model = CompanyTrigger()
        if include_optional:
            return CompanyTrigger(
                company_id = 5358233,
                api_version = 'v2',
                trigger = procore_sdk.models.company_trigger_trigger.company_trigger_trigger(
                    resource_name = 'Project Users', 
                    event_type = 'delete', )
            )
        else:
            return CompanyTrigger(
                company_id = 5358233,
                api_version = 'v2',
                trigger = procore_sdk.models.company_trigger_trigger.company_trigger_trigger(
                    resource_name = 'Project Users', 
                    event_type = 'delete', ),
        )
        """

    def testCompanyTrigger(self):
        """Test CompanyTrigger"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
