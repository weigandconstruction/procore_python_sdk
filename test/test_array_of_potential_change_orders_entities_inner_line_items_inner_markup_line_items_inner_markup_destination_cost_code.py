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

from procore_sdk.models.array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_markup_destination_cost_code import ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode

class TestArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode(unittest.TestCase):
    """ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode:
        """Test ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode`
        """
        model = ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode()
        if include_optional:
            return ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode(
                id = 12345,
                full_code = '02-300',
                name = 'Earthwork'
            )
        else:
            return ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode(
        )
        """

    def testArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode(self):
        """Test ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
