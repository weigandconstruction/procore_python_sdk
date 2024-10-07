# RFQChangeEventChangeEventLineItemsInnerBudgetMod

Budget Modification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Created at | [optional] 
**transfer_amount** | **float** | Amount transfered from the source Budget Line Item to the Target Budget Line Item | [optional] 
**notes** | **str** | Notes describing the modification | [optional] 
**from_budget_line_item_id** | **int** | Source line item id | [optional] 
**to_budget_line_item_id** | **int** | Target line item id | [optional] 

## Example

```python
from procore_sdk.models.rfq_change_event_change_event_line_items_inner_budget_mod import RFQChangeEventChangeEventLineItemsInnerBudgetMod

# TODO update the JSON string below
json = "{}"
# create an instance of RFQChangeEventChangeEventLineItemsInnerBudgetMod from a JSON string
rfq_change_event_change_event_line_items_inner_budget_mod_instance = RFQChangeEventChangeEventLineItemsInnerBudgetMod.from_json(json)
# print the JSON string representation of the object
print(RFQChangeEventChangeEventLineItemsInnerBudgetMod.to_json())

# convert the object into a dict
rfq_change_event_change_event_line_items_inner_budget_mod_dict = rfq_change_event_change_event_line_items_inner_budget_mod_instance.to_dict()
# create an instance of RFQChangeEventChangeEventLineItemsInnerBudgetMod from a dict
rfq_change_event_change_event_line_items_inner_budget_mod_from_dict = RFQChangeEventChangeEventLineItemsInnerBudgetMod.from_dict(rfq_change_event_change_event_line_items_inner_budget_mod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


