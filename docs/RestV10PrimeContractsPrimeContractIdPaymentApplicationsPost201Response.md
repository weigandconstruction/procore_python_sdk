# RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**g703** | [**List[RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201ResponseAllOfG703Inner]**](RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201ResponseAllOfG703Inner.md) |  | [optional] 
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
**description_type** | **str** | Description type to be shown for line items | [optional] [default to 'automatic']
**g702** | [**RestV10PaymentApplicationsGet200ResponseInnerAllOfG702**](RestV10PaymentApplicationsGet200ResponseInnerAllOfG702.md) |  | [optional] 
**billing_period** | [**RestV10PaymentApplicationsGet200ResponseInnerAllOfBillingPeriod**](RestV10PaymentApplicationsGet200ResponseInnerAllOfBillingPeriod.md) |  | [optional] 
**contract** | [**RestV10PaymentApplicationsGet200ResponseInnerAllOfContract**](RestV10PaymentApplicationsGet200ResponseInnerAllOfContract.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_prime_contracts_prime_contract_id_payment_applications_post201_response import RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response from a JSON string
rest_v10_prime_contracts_prime_contract_id_payment_applications_post201_response_instance = RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response.to_json())

# convert the object into a dict
rest_v10_prime_contracts_prime_contract_id_payment_applications_post201_response_dict = rest_v10_prime_contracts_prime_contract_id_payment_applications_post201_response_instance.to_dict()
# create an instance of RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response from a dict
rest_v10_prime_contracts_prime_contract_id_payment_applications_post201_response_from_dict = RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response.from_dict(rest_v10_prime_contracts_prime_contract_id_payment_applications_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


