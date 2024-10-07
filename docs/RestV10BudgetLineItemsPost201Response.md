# RestV10BudgetLineItemsPost201Response

Budget Line Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**original_budget_amount** | **float** | Original budget amount | [optional] 
**uom** | **str** | Unit of Measure | [optional] 
**quantity** | **float** | Quantity | [optional] 
**unit_cost** | **float** | Unit Cost | [optional] 
**calculation_strategy** | **str** | Calculation Strategy | [optional] 
**approved_budget_changes** | **float** | Approved budget changes | [optional] 
**revised_budget** | **float** | Revised budget | [optional] 
**pending_budget_changes** | **float** | Pending budget changes | [optional] 
**projected_budget** | **float** | Projected budget | [optional] 
**committed_costs** | **float** | Committed costs | [optional] 
**direct_costs** | **float** | Direct costs | [optional] 
**pending_cost_changes** | **float** | Pending cost changes | [optional] 
**projected_costs** | **float** | Projected costs | [optional] 
**budget_forecast** | **float** | Budget forecast | [optional] 
**estimated_cost_at_completion** | **float** | Estimated cost at completion | [optional] 
**projected_over_under** | **float** | Projected over under | [optional] 
**cost_code** | [**RestV10BudgetLineItemsPost201ResponseCostCode**](RestV10BudgetLineItemsPost201ResponseCostCode.md) |  | [optional] 
**division** | [**RestV10BudgetLineItemsPost201ResponseDivision**](RestV10BudgetLineItemsPost201ResponseDivision.md) |  | [optional] 
**line_item_type** | [**RestV10BudgetLineItemsPost201ResponseLineItemType**](RestV10BudgetLineItemsPost201ResponseLineItemType.md) |  | [optional] 
**currency_configuration** | [**RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration**](RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_budget_line_items_post201_response import RestV10BudgetLineItemsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BudgetLineItemsPost201Response from a JSON string
rest_v10_budget_line_items_post201_response_instance = RestV10BudgetLineItemsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10BudgetLineItemsPost201Response.to_json())

# convert the object into a dict
rest_v10_budget_line_items_post201_response_dict = rest_v10_budget_line_items_post201_response_instance.to_dict()
# create an instance of RestV10BudgetLineItemsPost201Response from a dict
rest_v10_budget_line_items_post201_response_from_dict = RestV10BudgetLineItemsPost201Response.from_dict(rest_v10_budget_line_items_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


