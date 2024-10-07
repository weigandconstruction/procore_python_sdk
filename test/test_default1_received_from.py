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

from procore_sdk.models.default1_received_from import Default1ReceivedFrom

class TestDefault1ReceivedFrom(unittest.TestCase):
    """Default1ReceivedFrom unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Default1ReceivedFrom:
        """Test Default1ReceivedFrom
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Default1ReceivedFrom`
        """
        model = Default1ReceivedFrom()
        if include_optional:
            return Default1ReceivedFrom(
                id = 161072,
                name = 'Carl the Contractor'
            )
        else:
            return Default1ReceivedFrom(
        )
        """

    def testDefault1ReceivedFrom(self):
        """Test Default1ReceivedFrom"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
