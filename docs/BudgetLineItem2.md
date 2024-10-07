# BudgetLineItem2

Budget Line Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_code_id** | **int** | Cost Code ID | 
**line_item_type_id** | **int** | Line Item Type ID | 
**original_budget_amount** | **float** | Original Budget amount | [optional] 
**uom** | **str** | Unit of Measure | [optional] 
**quantity** | **float** | Quantity | [optional] 
**unit_cost** | **float** | Unit Cost | [optional] 
**calculation_strategy** | **str** | Calculation Strategy | [optional] 

## Example

```python
from procore_sdk.models.budget_line_item2 import BudgetLineItem2

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetLineItem2 from a JSON string
budget_line_item2_instance = BudgetLineItem2.from_json(json)
# print the JSON string representation of the object
print(BudgetLineItem2.to_json())

# convert the object into a dict
budget_line_item2_dict = budget_line_item2_instance.to_dict()
# create an instance of BudgetLineItem2 from a dict
budget_line_item2_from_dict = BudgetLineItem2.from_dict(budget_line_item2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


