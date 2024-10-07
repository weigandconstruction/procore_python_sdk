# RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration

Payment Application (Owner Invoice) Currency Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_iso_code** | **str** | ISO Code for the Currency | [optional] 
**currency_exchange_rate** | **str** | Exchange rate for the Currency | [optional] 
**base_currency_iso_code** | **str** | ISO Code for the Base Currency Code | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_payment_applications_get200_response_inner_all_of_currency_configuration import RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration from a JSON string
rest_v10_payment_applications_get200_response_inner_all_of_currency_configuration_instance = RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration.from_json(json)
# print the JSON string representation of the object
print(RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration.to_json())

# convert the object into a dict
rest_v10_payment_applications_get200_response_inner_all_of_currency_configuration_dict = rest_v10_payment_applications_get200_response_inner_all_of_currency_configuration_instance.to_dict()
# create an instance of RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration from a dict
rest_v10_payment_applications_get200_response_inner_all_of_currency_configuration_from_dict = RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration.from_dict(rest_v10_payment_applications_get200_response_inner_all_of_currency_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


