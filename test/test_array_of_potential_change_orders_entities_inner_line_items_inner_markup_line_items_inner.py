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

from procore_sdk.models.array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner import ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner

class TestArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner(unittest.TestCase):
    """ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner:
        """Test ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner`
        """
        model = ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner()
        if include_optional:
            return ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner(
                id = 352362,
                amount = '',
                created_at = '2017-08-14T21:39:40Z',
                updated_at = '2017-08-14T21:39:40Z',
                markup = procore_sdk.models.array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_markup.arrayOfPotentialChangeOrders_entities_inner_line_items_inner_markup_line_items_inner_markup(
                    id = 462136, 
                    position = 1, 
                    markup_set = 'horizontal', 
                    name = 'Foo', 
                    percentage = '10', 
                    compounds_markups_above = False, 
                    created_at = '2017-08-14T21:39:40Z', 
                    updated_at = '2017-08-14T21:39:40Z', 
                    destination_cost_code = procore_sdk.models.array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_markup_destination_cost_code.arrayOfPotentialChangeOrders_entities_inner_line_items_inner_markup_line_items_inner_markup_destination_cost_code(
                        id = 12345, 
                        full_code = '02-300', 
                        name = 'Earthwork', ), 
                    destination_line_item_type = procore_sdk.models.line_item_type.LineItemType(
                        id = 12345, 
                        name = 'Equipment', 
                        code = 'LB', 
                        base_type = 'materials', 
                        origin_data = 'OD-2398273424', 
                        origin_id = 'ABC123', ), 
                    desitination_budget_line_item_id = 362262, 
                    destination_sub_job = null, ),
                currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                    currency_iso_code = 'USD', )
            )
        else:
            return ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner(
        )
        """

    def testArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner(self):
        """Test ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
