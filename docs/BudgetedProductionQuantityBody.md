# BudgetedProductionQuantityBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgeted_production_quantity** | [**BudgetedProductionQuantity**](BudgetedProductionQuantity.md) |  | 

## Example

```python
from procore_sdk.models.budgeted_production_quantity_body import BudgetedProductionQuantityBody

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetedProductionQuantityBody from a JSON string
budgeted_production_quantity_body_instance = BudgetedProductionQuantityBody.from_json(json)
# print the JSON string representation of the object
print(BudgetedProductionQuantityBody.to_json())

# convert the object into a dict
budgeted_production_quantity_body_dict = budgeted_production_quantity_body_instance.to_dict()
# create an instance of BudgetedProductionQuantityBody from a dict
budgeted_production_quantity_body_from_dict = BudgetedProductionQuantityBody.from_dict(budgeted_production_quantity_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


