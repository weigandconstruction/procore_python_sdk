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

from procore_sdk.models.bid_bid_items_inner import BidBidItemsInner

class TestBidBidItemsInner(unittest.TestCase):
    """BidBidItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BidBidItemsInner:
        """Test BidBidItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BidBidItemsInner`
        """
        model = BidBidItemsInner()
        if include_optional:
            return BidBidItemsInner(
                amount = 100000.0,
                bid_form_item_id = 223345,
                cost_code_id = 32780682,
                cost_code_name = 'Wood Sub-floors',
                cost_code_number = '00-01 39-12',
                id = 223345,
                included = True,
                quantity = '15.0',
                unit_cost = '900.0',
                uom = 'each'
            )
        else:
            return BidBidItemsInner(
        )
        """

    def testBidBidItemsInner(self):
        """Test BidBidItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
