# RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response

Payment Application (Owner Invoice) Contract Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**balance_to_finish** | **str** | Balance to finish amount | [optional] 
**materials_presently_stored** | **str** | Materials presently stored amount | [optional] 
**scheduled_value** | **str** | Scheduled value amount | [optional] 
**total_completed_and_stored_to_date** | **str** | Total completed and stored to date amount | [optional] 
**total_completed_and_stored_to_date_percent** | **str** | Total completed and stored to date percent | [optional] 
**work_completed_from_previous_application** | **str** | Work completed from previous application amount | [optional] 
**work_completed_this_period** | **str** | Work completed this period amount | [optional] 
**description_of_work** | **str** | Description of work | [optional] 
**item_number** | **int** | Item number | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**wbs_code** | [**WbsCode**](WbsCode.md) |  | [optional] 
**scheduled_unit_price** | **str** | Scheduled unit price | [optional] 
**scheduled_quantity** | **str** | Scheduled quantity | [optional] 
**total_completed_and_stored_to_date_quantity** | **str** | Total completed and stored to date quantity | [optional] 
**work_completed_this_period_quantity** | **str** | Work completed this period quantity | [optional] 
**work_completed_from_previous_application_quantity** | **str** | Work completed from previous application quantity | [optional] 
**work_completed_retainage_currently_retained** | **str** | Work completed retainage currently retained amount | [optional] 
**work_completed_retainage_from_previous_application** | **str** | Work completed retainage amount from previous application | [optional] 
**work_completed_retainage_released_this_period** | **str** | Work completed retainage amount released this period | [optional] 
**work_completed_retainage_retained_this_period** | **str** | Work completed retainage amount retained this period | [optional] 
**work_completed_retainage_percent_this_period** | **str** | Work completed retainage percent this period | [optional] 
**materials_stored_retainage_currently_retained** | **str** | Materials stored retainage amount currently retained | [optional] 
**materials_stored_retainage_from_previous_application** | **str** | Materials stored retainage amount from previous application | [optional] 
**materials_stored_retainage_released_this_period** | **str** | Materials stored retainage amount released this period | [optional] 
**materials_stored_retainage_retained_this_period** | **str** | Materials stored retainage amount retained this period | [optional] 
**materials_stored_retainage_percent_this_period** | **str** | Materials stored retainage percent this period | [optional] 
**total_retainage_currently_retained** | **str** | Total retainage amount currently retained | [optional] 
**total_retainage_from_previous_application** | **str** | Total retainage amount from previous application | [optional] 
**type** | **str** | Type of PaymentApplicationContractItem | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch200_response import RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response from a JSON string
rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch200_response_instance = RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response.to_json())

# convert the object into a dict
rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch200_response_dict = rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch200_response_instance.to_dict()
# create an instance of RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response from a dict
rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch200_response_from_dict = RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response.from_dict(rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


