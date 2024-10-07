# ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Markup ID | [optional] 
**position** | **int** | Position | [optional] 
**markup_set** | **str** | Markup set | [optional] 
**name** | **str** | name | [optional] 
**percentage** | **str** | Percentage | [optional] 
**compounds_markups_above** | **bool** | Compounds markups above? | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**destination_cost_code** | [**ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode**](ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode.md) |  | [optional] 
**destination_line_item_type** | [**LineItemType**](LineItemType.md) |  | [optional] 
**desitination_budget_line_item_id** | **int** | Destination Budget Line Item ID | [optional] 
**destination_sub_job** | [**RestV10SubJobsGet200ResponseInner**](RestV10SubJobsGet200ResponseInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_markup import ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkup

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkup from a JSON string
array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_markup_instance = ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkup.from_json(json)
# print the JSON string representation of the object
print(ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkup.to_json())

# convert the object into a dict
array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_markup_dict = array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_markup_instance.to_dict()
# create an instance of ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkup from a dict
array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_markup_from_dict = ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkup.from_dict(array_of_potential_change_orders_entities_inner_line_items_inner_markup_line_items_inner_markup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


