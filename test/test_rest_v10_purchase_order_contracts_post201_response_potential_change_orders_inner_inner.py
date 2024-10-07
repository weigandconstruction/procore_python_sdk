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

from procore_sdk.models.rest_v10_purchase_order_contracts_post201_response_potential_change_orders_inner_inner import RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner

class TestRestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner(unittest.TestCase):
    """RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner:
        """Test RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner`
        """
        model = RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner()
        if include_optional:
            return RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner(
                id = 2843048,
                contract_id = 304485,
                created_at = '2017-08-14T21:39:40Z',
                due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                invoiced_date = 'Fri Aug 18 00:00:00 UTC 2017',
                number = 'C34',
                paid_date = 'Fri Aug 18 00:00:00 UTC 2017',
                reviewed_at = '2017-08-19T21:39:40Z',
                status = 'draft',
                title = 'Concrete freezer slab',
                change_order_request_title = 'Concrete freezer slab',
                change_order_package_title = 'Concrete freezer slab',
                potential_change_order_acronym_number = 'PCO 95',
                change_order_request_acronym_number = 'COR 9001',
                change_order_package_acronym_number = 'CCO 42',
                change_order_tiers = 3,
                updated_at = '2017-08-16T21:39:40Z',
                currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                    currency_iso_code = 'USD', )
            )
        else:
            return RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner(
        )
        """

    def testRestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner(self):
        """Test RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
