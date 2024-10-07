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

from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_links import RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks

class TestRestV10ProjectsProjectIdBidPackagesPost201ResponseLinks(unittest.TestCase):
    """RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks:
        """Test RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks`
        """
        model = RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks()
        if include_optional:
            return RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks(
                add_vendor = '/159/project/bid_packages/75/vendors',
                analytics_events_path = '/rest/v1.0/analytic_events',
                attach_documents = '/159/project/bid_packages/75/attachments',
                bid_list = '/159/project/bid_packages/75/bidders',
                bid_packages = '/rest/v1.0/projects/159/bid_packages',
                bid_packages_by_project = '/159/project/bid_packages/75/search_for_bidders/filter_options/copy_bid_list_from',
                bulk_create_bids = '/159/project/bid_packages/75/bids/bulk_create',
                cost_codes = '/159/project/bid_packages/75/search_for_bidders/filter_options/standard_cost_codes',
                overview = '/159/project/bid_packages/75/overview',
                permission_templates = '/159/project/bid_packages/permission_templates',
                submit = '/159/project/bidding/bid_packages/75/add_to_bid_list',
                trades = '/159/project/bid_packages/75/search_for_bidders/filter_options/trades',
                vendors = '/159/project/bid_packages/75/vendors'
            )
        else:
            return RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks(
        )
        """

    def testRestV10ProjectsProjectIdBidPackagesPost201ResponseLinks(self):
        """Test RestV10ProjectsProjectIdBidPackagesPost201ResponseLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
