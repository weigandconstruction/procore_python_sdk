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

from procore_sdk.models.hazard import Hazard

class TestHazard(unittest.TestCase):
    """Hazard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Hazard:
        """Test Hazard
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Hazard`
        """
        model = Hazard()
        if include_optional:
            return Hazard(
                id = 1738,
                name = 'Slip',
                active = True,
                var_global = False,
                created_at = '2016-10-25T17:53:35Z',
                updated_at = '2016-10-25T17:53:35Z'
            )
        else:
            return Hazard(
        )
        """

    def testHazard(self):
        """Test Hazard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
