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

from procore_sdk.models.rfq_change_event_change_event_line_items_inner_links import RFQChangeEventChangeEventLineItemsInnerLinks

class TestRFQChangeEventChangeEventLineItemsInnerLinks(unittest.TestCase):
    """RFQChangeEventChangeEventLineItemsInnerLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RFQChangeEventChangeEventLineItemsInnerLinks:
        """Test RFQChangeEventChangeEventLineItemsInnerLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RFQChangeEventChangeEventLineItemsInnerLinks`
        """
        model = RFQChangeEventChangeEventLineItemsInnerLinks()
        if include_optional:
            return RFQChangeEventChangeEventLineItemsInnerLinks(
                edit = 'https://app.procore.com/22585/project/change_events/events/344096/edit?celi_id=336014#336014',
                view = 'https://app.procore.com/22585/project/change_events/events/344096?celi_id=336014#336014',
                contract = '',
                prime_pco_cost = '',
                commitment_contract_cost = '',
                commitment_pco_cost = '',
                rfq_amount = '',
                rom = ''
            )
        else:
            return RFQChangeEventChangeEventLineItemsInnerLinks(
        )
        """

    def testRFQChangeEventChangeEventLineItemsInnerLinks(self):
        """Test RFQChangeEventChangeEventLineItemsInnerLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
