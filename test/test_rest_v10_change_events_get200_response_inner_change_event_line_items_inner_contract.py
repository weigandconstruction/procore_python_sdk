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

from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_contract import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract

class TestRestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract(unittest.TestCase):
    """RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract:
        """Test RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract`
        """
        model = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract()
        if include_optional:
            return RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract(
                id = 853215,
                number = '001',
                title = 'PO--001',
                name = 'PO--001'
            )
        else:
            return RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract(
        )
        """

    def testRestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract(self):
        """Test RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
