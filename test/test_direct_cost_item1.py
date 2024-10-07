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

from procore_sdk.models.direct_cost_item1 import DirectCostItem1

class TestDirectCostItem1(unittest.TestCase):
    """DirectCostItem1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DirectCostItem1:
        """Test DirectCostItem1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DirectCostItem1`
        """
        model = DirectCostItem1()
        if include_optional:
            return DirectCostItem1(
                description = 'Home Depot Purchase',
                employee_id = 14522,
                direct_cost_date = 'Wed Dec 14 00:00:00 UTC 2016',
                origin_data = 'OD-2398273424',
                origin_id = 'px-1990',
                payment_date = 'Thu Jan 05 00:00:00 UTC 2017',
                received_date = 'Tue Jan 10 00:00:00 UTC 2017',
                status = 'approved',
                terms = 'Net 30',
                vendor_id = 43122,
                line_items = [
                    procore_sdk.models.direct_cost_line_item.Direct Cost Line Item(
                        id = 1234, 
                        manual_amount = 1000, 
                        wbs_code_id = 1989, 
                        description = '100' of Copper Piping', 
                        direct_cost_id = 81753, 
                        origin_data = 'OD-2398273424', 
                        origin_id = 'px-1990', 
                        quantity = 82.0201, 
                        ref = 'PQRS5678', 
                        unit_cost = 12.03, 
                        uom = 'cubic feet', )
                    ]
            )
        else:
            return DirectCostItem1(
        )
        """

    def testDirectCostItem1(self):
        """Test DirectCostItem1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
