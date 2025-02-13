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

from procore_sdk.models.direct_cost_item2 import DirectCostItem2

class TestDirectCostItem2(unittest.TestCase):
    """DirectCostItem2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DirectCostItem2:
        """Test DirectCostItem2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DirectCostItem2`
        """
        model = DirectCostItem2()
        if include_optional:
            return DirectCostItem2(
                description = 'Invoice for April',
                direct_cost_date = 'Wed Dec 14 00:00:00 UTC 2016',
                employee_id = 43223,
                invoice_number = 'Invoice # abc123',
                origin_data = 'OD-2398273424',
                origin_id = '23423',
                payment_date = 'Tue Jan 10 00:00:00 UTC 2017',
                received_date = 'Sun Jan 08 00:00:00 UTC 2017',
                status = 'approved',
                terms = 'Net 50',
                vendor_id = 23423,
                direct_cost_type = 'invoice'
            )
        else:
            return DirectCostItem2(
                invoice_number = 'Invoice # abc123',
                vendor_id = 23423,
                direct_cost_type = 'invoice',
        )
        """

    def testDirectCostItem2(self):
        """Test DirectCostItem2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
