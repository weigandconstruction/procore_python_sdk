# ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Line Item ID | [optional] 
**position** | **int** | Postion | [optional] 
**description** | **str** | Description | [optional] 
**quantity** | **float** | Quantity | [optional] 
**uom** | **str** | Unit of measurement | [optional] 
**total_amount** | **float** | Total amount | [optional] 
**extended_amount** | **float** | Extended amount | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**tax_code_id** | **int** | Tax Code ID | [optional] 
**unit_cost** | **float** | Unit cost | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**line_item_type** | [**LineItemType**](LineItemType.md) |  | [optional] 
**markup_line_items** | [**List[ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner]**](ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_potential_change_orders_entities_inner_line_items_inner import ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInner from a JSON string
array_of_potential_change_orders_entities_inner_line_items_inner_instance = ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInner.to_json())

# convert the object into a dict
array_of_potential_change_orders_entities_inner_line_items_inner_dict = array_of_potential_change_orders_entities_inner_line_items_inner_instance.to_dict()
# create an instance of ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInner from a dict
array_of_potential_change_orders_entities_inner_line_items_inner_from_dict = ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInner.from_dict(array_of_potential_change_orders_entities_inner_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


