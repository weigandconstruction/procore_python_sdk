# DirectCostLineItem1CurrencyConfiguration

Payment Application (Owner Invoice) Currency Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_iso_code** | **str** | ISO Code for the Currency | [optional] 
**base_currency_iso_code** | **str** | Base currency ISO code | [optional] 
**currency_exchange_rate** | **float** | Currency exchange rate | [optional] 

## Example

```python
from procore_sdk.models.direct_cost_line_item1_currency_configuration import DirectCostLineItem1CurrencyConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DirectCostLineItem1CurrencyConfiguration from a JSON string
direct_cost_line_item1_currency_configuration_instance = DirectCostLineItem1CurrencyConfiguration.from_json(json)
# print the JSON string representation of the object
print(DirectCostLineItem1CurrencyConfiguration.to_json())

# convert the object into a dict
direct_cost_line_item1_currency_configuration_dict = direct_cost_line_item1_currency_configuration_instance.to_dict()
# create an instance of DirectCostLineItem1CurrencyConfiguration from a dict
direct_cost_line_item1_currency_configuration_from_dict = DirectCostLineItem1CurrencyConfiguration.from_dict(direct_cost_line_item1_currency_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


