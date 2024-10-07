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

from procore_sdk.models.body72 import Body72

class TestBody72(unittest.TestCase):
    """Body72 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body72:
        """Test Body72
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body72`
        """
        model = Body72()
        if include_optional:
            return Body72(
                location = procore_sdk.models.location.Location(
                    path = ["North Building","First Floor","Electrical Closet"], )
            )
        else:
            return Body72(
                location = procore_sdk.models.location.Location(
                    path = ["North Building","First Floor","Electrical Closet"], ),
        )
        """

    def testBody72(self):
        """Test Body72"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
