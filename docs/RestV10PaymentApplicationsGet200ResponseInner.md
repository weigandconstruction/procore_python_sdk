# RestV10PaymentApplicationsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**billing_date** | **date** | Billing date | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**origin_data** | **str** | Payment Application (Owner Invoice) third party data | [optional] 
**origin_id** | **str** | Payment Application (Owner Invoice) third party ID | [optional] 
**percent_complete** | **str** | Percent complete | [optional] 
**period_start** | **date** | Period start date | [optional] 
**period_end** | **date** | Period end date | [optional] 
**period_id** | **int** | Billing Period Identifier | [optional] 
**status** | **str** | Status | [optional] 
**total_amount_paid** | **str** | Total amount of Payments made to the Payment Application | [optional] 
**number** | **int** | Payment Application (Owner Invoice) number | [optional] 
**total_amount_accrued_this_period** | **str** | Gross amount of the Invoice. | [optional] 
**formatted_contract_company** | **str** | Name of the Owner/Client of the Invoice. | [optional] 
**currency_configuration** | [**RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration**](RestV10PaymentApplicationsGet200ResponseInnerAllOfCurrencyConfiguration.md) |  | [optional] 
**g702** | [**RestV10PaymentApplicationsGet200ResponseInnerAllOfG702**](RestV10PaymentApplicationsGet200ResponseInnerAllOfG702.md) |  | [optional] 
**billing_period** | [**RestV10PaymentApplicationsGet200ResponseInnerAllOfBillingPeriod**](RestV10PaymentApplicationsGet200ResponseInnerAllOfBillingPeriod.md) |  | [optional] 
**contract** | [**RestV10PaymentApplicationsGet200ResponseInnerAllOfContract**](RestV10PaymentApplicationsGet200ResponseInnerAllOfContract.md) |  | [optional] 
**created_at** | **date** | When the payment application was created | [optional] 
**updated_at** | **date** | When the payment application was last updated | [optional] 
**description_type** | **str** | Description type to be shown for line items | [optional] [default to 'automatic']

## Example

```python
from procore_sdk.models.rest_v10_payment_applications_get200_response_inner import RestV10PaymentApplicationsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PaymentApplicationsGet200ResponseInner from a JSON string
rest_v10_payment_applications_get200_response_inner_instance = RestV10PaymentApplicationsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10PaymentApplicationsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_payment_applications_get200_response_inner_dict = rest_v10_payment_applications_get200_response_inner_instance.to_dict()
# create an instance of RestV10PaymentApplicationsGet200ResponseInner from a dict
rest_v10_payment_applications_get200_response_inner_from_dict = RestV10PaymentApplicationsGet200ResponseInner.from_dict(rest_v10_payment_applications_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


