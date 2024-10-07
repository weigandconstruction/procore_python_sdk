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

from procore_sdk.models.location2 import Location2

class TestLocation2(unittest.TestCase):
    """Location2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Location2:
        """Test Location2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Location2`
        """
        model = Location2()
        if include_optional:
            return Location2(
                id = 15504,
                name = 'North Building>First Floor>Electrical Closet',
                node_name = 'Electrical Closet',
                parent_id = 788866,
                created_at = '2016-08-01T23:33:54Z',
                updated_at = '2016-08-01T23:33:54Z'
            )
        else:
            return Location2(
        )
        """

    def testLocation2(self):
        """Test Location2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
