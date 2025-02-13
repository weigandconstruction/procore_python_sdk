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

from procore_sdk.models.bid_recipient_list_inner import BidRecipientListInner

class TestBidRecipientListInner(unittest.TestCase):
    """BidRecipientListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BidRecipientListInner:
        """Test BidRecipientListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BidRecipientListInner`
        """
        model = BidRecipientListInner()
        if include_optional:
            return BidRecipientListInner(
                first = 'John',
                last = 'Doe',
                email = 'j.doe@example.com',
                numbers = 'Office: N/A, Mobile: 805.123.1234'
            )
        else:
            return BidRecipientListInner(
        )
        """

    def testBidRecipientListInner(self):
        """Test BidRecipientListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
