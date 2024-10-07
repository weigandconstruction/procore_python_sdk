# BudgetModification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_budget_line_item_id** | **int** | ID of the Budget Line Item to transfer from. NOTE 1: required if &#39;Allow Budget Modifications Which Modify Grand Total&#39; is not checked. NOTE 2: When updating if you want to remove the from_budget_line_item_id reference pass in NULL as the value. NOTE 3: You may not pass the same from_budget_line_item_id as to_budget_line_item_id. | [optional] 
**notes** | **str** | Notes on the purpose of the transfer | [optional] 
**origin_data** | **str** | The Origin Data to associate with this Budget Modification | [optional] 
**origin_id** | **str** | The Origin ID to associate with this Budget Modification (must be unique within a company) | [optional] 
**to_budget_line_item_id** | **int** | ID of the Budget Line Item to transfer to. NOTE: You may not pass the same to_budget_line_item_id as from_budget_line_item_id. | 
**transfer_amount** | **float** | Transfer amount | 

## Example

```python
from procore_sdk.models.budget_modification import BudgetModification

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetModification from a JSON string
budget_modification_instance = BudgetModification.from_json(json)
# print the JSON string representation of the object
print(BudgetModification.to_json())

# convert the object into a dict
budget_modification_dict = budget_modification_instance.to_dict()
# create an instance of BudgetModification from a dict
budget_modification_from_dict = BudgetModification.from_dict(budget_modification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


