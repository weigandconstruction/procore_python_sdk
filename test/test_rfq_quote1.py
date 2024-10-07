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

from procore_sdk.models.rfq_quote1 import RFQQuote1

class TestRFQQuote1(unittest.TestCase):
    """RFQQuote1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RFQQuote1:
        """Test RFQQuote1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RFQQuote1`
        """
        model = RFQQuote1()
        if include_optional:
            return RFQQuote1(
                commitment_quote_number = '45',
                cost = 3653,
                description = 'Need to rip out and reinstall windows. Keep the painter out of the area.',
                schedule_impact = 145
            )
        else:
            return RFQQuote1(
        )
        """

    def testRFQQuote1(self):
        """Test RFQQuote1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
