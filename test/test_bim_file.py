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

from procore_sdk.models.bim_file import BIMFile

class TestBIMFile(unittest.TestCase):
    """BIMFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BIMFile:
        """Test BIMFile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BIMFile`
        """
        model = BIMFile()
        if include_optional:
            return BIMFile(
                name = '101_BUILDING.NWF',
                uuid = 'a00147dd-a698-468a-b082-d277a564cf0c'
            )
        else:
            return BIMFile(
                name = '101_BUILDING.NWF',
                uuid = 'a00147dd-a698-468a-b082-d277a564cf0c',
        )
        """

    def testBIMFile(self):
        """Test BIMFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
