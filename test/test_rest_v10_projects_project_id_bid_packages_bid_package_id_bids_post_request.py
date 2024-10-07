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

from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request import RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest

class TestRestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest:
        """Test RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest`
        """
        model = RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest(
                bid = procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request_bid.RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPost_request_bid(
                    vendor_id = 3859014, 
                    lump_sum_amount = 10000, 
                    bidder_comments = 'Test Bid Comment', 
                    is_bidder_committed = True, 
                    submitted = True, 
                    recipient_ids = [1751318,1837467], )
            )
        else:
            return RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest(
        )
        """

    def testRestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest(self):
        """Test RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
