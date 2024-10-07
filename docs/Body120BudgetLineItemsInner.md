# Body120BudgetLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wbs_code_id** | **int** | Work Breakdown Structure Code ID | 
**original_budget_amount** | **float** | Original Budget amount | [optional] 
**uom** | **str** | Unit of Measure | [optional] 
**quantity** | **float** | Quantity | [optional] 
**unit_cost** | **float** | Unit Cost | [optional] 
**calculation_strategy** | **str** | Calculation Strategy | [optional] 
**id** | **int** | Budget Line Item ID | [optional] 

## Example

```python
from procore_sdk.models.body120_budget_line_items_inner import Body120BudgetLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body120BudgetLineItemsInner from a JSON string
body120_budget_line_items_inner_instance = Body120BudgetLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(Body120BudgetLineItemsInner.to_json())

# convert the object into a dict
body120_budget_line_items_inner_dict = body120_budget_line_items_inner_instance.to_dict()
# create an instance of Body120BudgetLineItemsInner from a dict
body120_budget_line_items_inner_from_dict = Body120BudgetLineItemsInner.from_dict(body120_budget_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


