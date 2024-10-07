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

from procore_sdk.models.company_trigger2 import CompanyTrigger2

class TestCompanyTrigger2(unittest.TestCase):
    """CompanyTrigger2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyTrigger2:
        """Test CompanyTrigger2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyTrigger2`
        """
        model = CompanyTrigger2()
        if include_optional:
            return CompanyTrigger2(
                company_id = 5358233,
                triggers = [42,43]
            )
        else:
            return CompanyTrigger2(
                company_id = 5358233,
                triggers = [42,43],
        )
        """

    def testCompanyTrigger2(self):
        """Test CompanyTrigger2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
