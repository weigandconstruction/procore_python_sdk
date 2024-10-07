# RestV11BudgetLineItemsPost201ResponseWbsCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Wbs Code ID | [optional] 
**flat_code** | **str** | Wbs Code | [optional] 
**description** | **str** | Wbs Code Description | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_budget_line_items_post201_response_wbs_code import RestV11BudgetLineItemsPost201ResponseWbsCode

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11BudgetLineItemsPost201ResponseWbsCode from a JSON string
rest_v11_budget_line_items_post201_response_wbs_code_instance = RestV11BudgetLineItemsPost201ResponseWbsCode.from_json(json)
# print the JSON string representation of the object
print(RestV11BudgetLineItemsPost201ResponseWbsCode.to_json())

# convert the object into a dict
rest_v11_budget_line_items_post201_response_wbs_code_dict = rest_v11_budget_line_items_post201_response_wbs_code_instance.to_dict()
# create an instance of RestV11BudgetLineItemsPost201ResponseWbsCode from a dict
rest_v11_budget_line_items_post201_response_wbs_code_from_dict = RestV11BudgetLineItemsPost201ResponseWbsCode.from_dict(rest_v11_budget_line_items_post201_response_wbs_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


