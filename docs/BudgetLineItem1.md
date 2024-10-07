# BudgetLineItem1

Budget Line Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wbs_code_id** | **int** | Work Breakdown Structure Code ID | [optional] 
**original_budget_amount** | **float** | Original Budget amount | [optional] 
**uom** | **str** | Unit of Measure | [optional] 
**quantity** | **float** | Quantity | [optional] 
**unit_cost** | **float** | Unit Cost | [optional] 
**calculation_strategy** | **str** | Calculation Strategy | [optional] 

## Example

```python
from procore_sdk.models.budget_line_item1 import BudgetLineItem1

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetLineItem1 from a JSON string
budget_line_item1_instance = BudgetLineItem1.from_json(json)
# print the JSON string representation of the object
print(BudgetLineItem1.to_json())

# convert the object into a dict
budget_line_item1_dict = budget_line_item1_instance.to_dict()
# create an instance of BudgetLineItem1 from a dict
budget_line_item1_from_dict = BudgetLineItem1.from_dict(budget_line_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


