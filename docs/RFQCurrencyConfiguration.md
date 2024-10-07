# RFQCurrencyConfiguration

currency configuration information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_iso_code** | **str** | currency ISO code | [optional] 

## Example

```python
from procore_sdk.models.rfq_currency_configuration import RFQCurrencyConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RFQCurrencyConfiguration from a JSON string
rfq_currency_configuration_instance = RFQCurrencyConfiguration.from_json(json)
# print the JSON string representation of the object
print(RFQCurrencyConfiguration.to_json())

# convert the object into a dict
rfq_currency_configuration_dict = rfq_currency_configuration_instance.to_dict()
# create an instance of RFQCurrencyConfiguration from a dict
rfq_currency_configuration_from_dict = RFQCurrencyConfiguration.from_dict(rfq_currency_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


