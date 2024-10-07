# RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration

Currency configuration object, the currency for the budget line item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_iso_code** | **str** | Currency Configuration ISO code | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_budget_line_items_post201_response_currency_configuration import RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration from a JSON string
rest_v11_budget_line_items_post201_response_currency_configuration_instance = RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration.from_json(json)
# print the JSON string representation of the object
print(RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration.to_json())

# convert the object into a dict
rest_v11_budget_line_items_post201_response_currency_configuration_dict = rest_v11_budget_line_items_post201_response_currency_configuration_instance.to_dict()
# create an instance of RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration from a dict
rest_v11_budget_line_items_post201_response_currency_configuration_from_dict = RestV11BudgetLineItemsPost201ResponseCurrencyConfiguration.from_dict(rest_v11_budget_line_items_post201_response_currency_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


