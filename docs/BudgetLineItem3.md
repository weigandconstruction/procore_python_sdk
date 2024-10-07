# BudgetLineItem3

Budget Line Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_code_id** | **int** | Cost Code ID | [optional] 
**line_item_type_id** | **int** | Line Item Type ID | [optional] 
**original_budget_amount** | **float** | Original Budget amount | [optional] 
**uom** | **str** | Unit of Measure | [optional] 
**quantity** | **float** | Quantity | [optional] 
**unit_cost** | **float** | Unit Cost | [optional] 
**calculation_strategy** | **str** | Calculation Strategy | [optional] 
**direct_costs** | **float** | Direct Costs (Include only if Direct Cost tool is turned off.) | [optional] 

## Example

```python
from procore_sdk.models.budget_line_item3 import BudgetLineItem3

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetLineItem3 from a JSON string
budget_line_item3_instance = BudgetLineItem3.from_json(json)
# print the JSON string representation of the object
print(BudgetLineItem3.to_json())

# convert the object into a dict
budget_line_item3_dict = budget_line_item3_instance.to_dict()
# create an instance of BudgetLineItem3 from a dict
budget_line_item3_from_dict = BudgetLineItem3.from_dict(budget_line_item3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


