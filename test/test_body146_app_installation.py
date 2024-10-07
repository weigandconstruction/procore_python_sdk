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

from procore_sdk.models.body146_app_installation import Body146AppInstallation

class TestBody146AppInstallation(unittest.TestCase):
    """Body146AppInstallation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body146AppInstallation:
        """Test Body146AppInstallation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body146AppInstallation`
        """
        model = Body146AppInstallation()
        if include_optional:
            return Body146AppInstallation(
                installation_configuration = {"url":"www.example.com"}
            )
        else:
            return Body146AppInstallation(
        )
        """

    def testBody146AppInstallation(self):
        """Test Body146AppInstallation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
