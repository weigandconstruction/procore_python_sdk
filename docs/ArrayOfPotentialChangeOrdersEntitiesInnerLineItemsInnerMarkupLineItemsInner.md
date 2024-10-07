# ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Markup Line Item ID | [optional] 
**amount** | **str** | Markup Line Item amount | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**markup** | [**ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkup**](ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkup.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner import ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner from a JSON string
array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_instance = ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner.to_json())

# convert the object into a dict
array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_dict = array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_instance.to_dict()
# create an instance of ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner from a dict
array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_from_dict = ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInner.from_dict(array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


