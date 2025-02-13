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

from procore_sdk.models.rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid import RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid

class TestRestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid(unittest.TestCase):
    """RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid:
        """Test RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid`
        """
        model = RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid()
        if include_optional:
            return RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid(
                lump_sum_amount = 10000,
                bidder_comments = 'Test Bid Comment',
                bidder_inclusion = 'Include Concrete',
                bidder_exclusion = 'Exclude Plumbing',
                bid_status = 'not_invited',
                is_bidder_committed = True,
                submitted = True,
                prostore_file_ids = [1751318,1837467],
                recipient_ids = [1751318,1837467],
                bid_items = [
                    procore_sdk.models.rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_bid_items_inner.RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatch_request_bid_bid_items_inner(
                        id = 123124112, 
                        bid_form_item_id = 32780682, 
                        cost_code_id = 32780682, 
                        amount = 100000, 
                        unit_cost = '900', 
                        quantity = '15', 
                        uom = 'pounds', )
                    ],
                bid_items_to_delete = [1234324,4992392]
            )
        else:
            return RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid(
        )
        """

    def testRestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid(self):
        """Test RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
