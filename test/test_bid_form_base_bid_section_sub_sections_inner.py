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

from procore_sdk.models.bid_form_base_bid_section_sub_sections_inner import BidFormBaseBidSectionSubSectionsInner

class TestBidFormBaseBidSectionSubSectionsInner(unittest.TestCase):
    """BidFormBaseBidSectionSubSectionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BidFormBaseBidSectionSubSectionsInner:
        """Test BidFormBaseBidSectionSubSectionsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BidFormBaseBidSectionSubSectionsInner`
        """
        model = BidFormBaseBidSectionSubSectionsInner()
        if include_optional:
            return BidFormBaseBidSectionSubSectionsInner(
                id = 75414,
                title = 'Concrete',
                position = 1,
                section_totals = [
                    procore_sdk.models.bid_form_base_bid_section_section_totals_inner.Bid_Form_base_bid_section_section_totals_inner(
                        bid_id = 392, 
                        vendor_id = 714, 
                        vendor_name = 'Bob McAdoo', 
                        total = 12039.55, )
                    ],
                bid_form_items = [
                    procore_sdk.models.bid_form_base_bid_section_bid_form_items_inner.Bid_Form_base_bid_section_bid_form_items_inner(
                        id = 75414, 
                        cost_code_id = 75414, 
                        full_code = '1-11 - Project Engineer', 
                        name = 'Project Engineer', 
                        description = 'Describing Project Engineer', 
                        number = '1-11', 
                        item_type = 'cost_code', 
                        subject = 'Dry wall raw material', 
                        response_type = 'amount', 
                        bid_items = [
                            procore_sdk.models.bid_form_base_bid_section_bid_form_items_inner_bid_items_inner.Bid_Form_base_bid_section_bid_form_items_inner_bid_items_inner(
                                id = 100, 
                                bid_id = 392, 
                                bid_item_id = 75414, 
                                vendor_id = 75414, 
                                amount = 12039.55, 
                                unit_cost = '$15.00', 
                                quantity = '5', 
                                uom = '1-11', 
                                included = True, )
                            ], )
                    ]
            )
        else:
            return BidFormBaseBidSectionSubSectionsInner(
        )
        """

    def testBidFormBaseBidSectionSubSectionsInner(self):
        """Test BidFormBaseBidSectionSubSectionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
