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

from procore_sdk.models.rfq_change_event_change_event_line_items_inner_contract import RFQChangeEventChangeEventLineItemsInnerContract

class TestRFQChangeEventChangeEventLineItemsInnerContract(unittest.TestCase):
    """RFQChangeEventChangeEventLineItemsInnerContract unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RFQChangeEventChangeEventLineItemsInnerContract:
        """Test RFQChangeEventChangeEventLineItemsInnerContract
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RFQChangeEventChangeEventLineItemsInnerContract`
        """
        model = RFQChangeEventChangeEventLineItemsInnerContract()
        if include_optional:
            return RFQChangeEventChangeEventLineItemsInnerContract(
                id = 11353,
                number = '001'
            )
        else:
            return RFQChangeEventChangeEventLineItemsInnerContract(
        )
        """

    def testRFQChangeEventChangeEventLineItemsInnerContract(self):
        """Test RFQChangeEventChangeEventLineItemsInnerContract"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
