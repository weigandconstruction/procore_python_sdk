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

from procore_sdk.models.bid_package import BidPackage

class TestBidPackage(unittest.TestCase):
    """BidPackage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BidPackage:
        """Test BidPackage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BidPackage`
        """
        model = BidPackage()
        if include_optional:
            return BidPackage(
                bid_due_date = '2016-12-13T03:00Z',
                bid_email_message = 'Procore would like to invite you to bid on new campus',
                bid_web_message = 'Please reach out to our help desk if you need assistance with bidding.',
                title = 'Procore Sky Campus',
                accounting_method = 'unit',
                bid_submission_confirmation = 'Your Bid Has Been Successfully Submitted',
                anticipated_award_date = 'Tue Dec 13 00:00:00 UTC 2016',
                number = '46',
                distribution_ids = [
                    1587816
                    ],
                blind_bidding = False,
                pre_bid_walk_through_date = '2016-12-13T03:00Z',
                pre_bid_walk_through_notes = 'So Many Potential Change Orders',
                enable_prebid_walkthrough = True,
                manager_id = 1587816
            )
        else:
            return BidPackage(
                bid_due_date = '2016-12-13T03:00Z',
                bid_email_message = 'Procore would like to invite you to bid on new campus',
                bid_web_message = 'Please reach out to our help desk if you need assistance with bidding.',
                title = 'Procore Sky Campus',
        )
        """

    def testBidPackage(self):
        """Test BidPackage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
