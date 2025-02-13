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

from procore_sdk.models.rest_v10_purchase_order_contracts_post201_response_change_order_packages_inner import RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner

class TestRestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner(unittest.TestCase):
    """RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner:
        """Test RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner`
        """
        model = RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner()
        if include_optional:
            return RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner(
                id = 239475,
                contract_id = 64545,
                created_at = '2016-10-23T21:39:40Z',
                deleted_at = '2017-07-29T21:39:40Z',
                due_date = 'Sun Oct 23 00:00:00 UTC 2016',
                invoiced_date = 'Sun Oct 09 00:00:00 UTC 2016',
                number = 'H-38',
                origin_code = 'ABC-123',
                origin_data = 'OD-123654789',
                origin_id = '654987123',
                paid_date = 'Sat Oct 22 00:00:00 UTC 2016',
                reviewed_at = '2016-10-24T15:42:33Z',
                signed_change_order_received_date = 'Sun Oct 23 00:00:00 UTC 2016',
                status = 'draft',
                title = 'Additional Time & Materials',
                updated_at = '2016-10-23T21:39:40Z',
                currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                    currency_iso_code = 'USD', )
            )
        else:
            return RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner(
        )
        """

    def testRestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner(self):
        """Test RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
