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

from procore_sdk.models.body56 import Body56

class TestBody56(unittest.TestCase):
    """Body56 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body56:
        """Test Body56
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body56`
        """
        model = Body56()
        if include_optional:
            return Body56(
                project_id = 56,
                observation = procore_sdk.models.observation.Observation()
            )
        else:
            return Body56(
                project_id = 56,
                observation = procore_sdk.models.observation.Observation(),
        )
        """

    def testBody56(self):
        """Test Body56"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
