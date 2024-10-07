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

from procore_sdk.models.body144_base_bid_inner_bid_form_items_inner import Body144BaseBidInnerBidFormItemsInner

class TestBody144BaseBidInnerBidFormItemsInner(unittest.TestCase):
    """Body144BaseBidInnerBidFormItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body144BaseBidInnerBidFormItemsInner:
        """Test Body144BaseBidInnerBidFormItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body144BaseBidInnerBidFormItemsInner`
        """
        model = Body144BaseBidInnerBidFormItemsInner()
        if include_optional:
            return Body144BaseBidInnerBidFormItemsInner(
                id = 1235,
                cost_code_id = 1,
                description = 'Concrete',
                position = 1,
                subject = 'Is the insurance of tools included in the Bid?',
                item_type = 'cost_code',
                response_type = 'amount'
            )
        else:
            return Body144BaseBidInnerBidFormItemsInner(
        )
        """

    def testBody144BaseBidInnerBidFormItemsInner(self):
        """Test Body144BaseBidInnerBidFormItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
