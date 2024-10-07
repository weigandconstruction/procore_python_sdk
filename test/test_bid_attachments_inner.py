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

from procore_sdk.models.bid_attachments_inner import BidAttachmentsInner

class TestBidAttachmentsInner(unittest.TestCase):
    """BidAttachmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BidAttachmentsInner:
        """Test BidAttachmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BidAttachmentsInner`
        """
        model = BidAttachmentsInner()
        if include_optional:
            return BidAttachmentsInner(
                id = 5324,
                item_type = 'Bid',
                prostore_file_id = 1234,
                url = 'http://www.example.com/',
                name = 'january_receipt_copy.jpg'
            )
        else:
            return BidAttachmentsInner(
        )
        """

    def testBidAttachmentsInner(self):
        """Test BidAttachmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
