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

from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_company import RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany

class TestRestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany(unittest.TestCase):
    """RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany:
        """Test RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany`
        """
        model = RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany()
        if include_optional:
            return RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany(
                id = 163215,
                name = 'Procore Tech'
            )
        else:
            return RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany(
        )
        """

    def testRestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany(self):
        """Test RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
