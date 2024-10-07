# RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod

Budget Modification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Created at | [optional] 
**transfer_amount** | **float** | Amount transfered from the source Budget Line Item to the Target Budget Line Item | [optional] 
**notes** | **str** | Notes describing the modification | [optional] 
**from_budget_line_item_id** | **int** | Source line item id | [optional] 
**to_budget_line_item_id** | **int** | Target line item id | [optional] 
**from_budget_line_item_name** | **str** | Source line item name | [optional] 
**to_budget_line_item_name** | **str** | Target line item name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_mod import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod from a JSON string
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_mod_instance = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod.to_json())

# convert the object into a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_mod_dict = rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_mod_instance.to_dict()
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod from a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_mod_from_dict = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod.from_dict(rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_mod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


