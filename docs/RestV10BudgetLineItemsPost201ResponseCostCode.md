# RestV10BudgetLineItemsPost201ResponseCostCode

Cost Code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**code** | **str** | Cost code | [optional] 
**full_code** | **str** | Cost full code | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_line_items_post201_response_cost_code import RestV10BudgetLineItemsPost201ResponseCostCode

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetLineItemsPost201ResponseCostCode from a JSON string
rest_v10_budget_line_items_post201_response_cost_code_instance = RestV10BudgetLineItemsPost201ResponseCostCode.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetLineItemsPost201ResponseCostCode.to_json())

# convert the object into a dict
rest_v10_budget_line_items_post201_response_cost_code_dict = rest_v10_budget_line_items_post201_response_cost_code_instance.to_dict()
# create an instance of RestV10BudgetLineItemsPost201ResponseCostCode from a dict
rest_v10_budget_line_items_post201_response_cost_code_from_dict = RestV10BudgetLineItemsPost201ResponseCostCode.from_dict(rest_v10_budget_line_items_post201_response_cost_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


