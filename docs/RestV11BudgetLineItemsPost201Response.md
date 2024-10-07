# RestV11BudgetLineItemsPost201Response

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
**wbs_code** | [**RestV11BudgetLineItemsPost201ResponseWbsCode**](RestV11BudgetLineItemsPost201ResponseWbsCode.md) |  | [optional] 
**currency_configuration** | [**RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration**](RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_budget_line_items_post201_response import RestV11BudgetLineItemsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11BudgetLineItemsPost201Response from a JSON string
rest_v11_budget_line_items_post201_response_instance = RestV11BudgetLineItemsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV11BudgetLineItemsPost201Response.to_json())

# convert the object into a dict
rest_v11_budget_line_items_post201_response_dict = rest_v11_budget_line_items_post201_response_instance.to_dict()
# create an instance of RestV11BudgetLineItemsPost201Response from a dict
rest_v11_budget_line_items_post201_response_from_dict = RestV11BudgetLineItemsPost201Response.from_dict(rest_v11_budget_line_items_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


