# BudgetedProductionQuantity

Budgeted Production Quantity Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project | [optional] 
**cost_code_id** | **int** | CostCode.  DO NOT provide if your project is configured for Task Codes. | [optional] 
**wbs_code_id** | **int** | The Production Quantity Code for the Budgeted Production Quantity. This is necessary if your project is configured for Task Codes. DO NOT provide if your project is not configured for Task Codes. | [optional] 
**quantity** | **float** | Quantity budgeted for a project cost code | [optional] 
**unit_of_measure** | **str** | Unit of Measure | [optional] 

## Example

```python
from procore_sdk.models.budgeted_production_quantity import BudgetedProductionQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetedProductionQuantity from a JSON string
budgeted_production_quantity_instance = BudgetedProductionQuantity.from_json(json)
# print the JSON string representation of the object
print(BudgetedProductionQuantity.to_json())

# convert the object into a dict
budgeted_production_quantity_dict = budgeted_production_quantity_instance.to_dict()
# create an instance of BudgetedProductionQuantity from a dict
budgeted_production_quantity_from_dict = BudgetedProductionQuantity.from_dict(budgeted_production_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


