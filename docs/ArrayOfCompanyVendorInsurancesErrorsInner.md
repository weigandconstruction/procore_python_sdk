# ArrayOfCompanyVendorInsurancesErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**effective_date** | **date** | Effective date | [optional] 
**enable_expired_insurance_notifications** | **bool** | Enable/Disable expired insurance notifications | [optional] 
**exempt** | **bool** | Exempt status | [optional] 
**expiration_date** | **date** | Expiration date | [optional] 
**info_received** | **bool** | Information received (or not) | [optional] 
**insurance_provider** | **str** | Insurance provider | [optional] 
**insurance_type** | **str** | Insurance type | [optional] 
**limit** | **str** | Limit | [optional] 
**notes** | **str** | Notes | [optional] 
**policy_number** | **str** | Policy number | [optional] 
**status** | **str** | Status | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 
**additional_insured** | **str** | Additional Individuals and/or Companies Insured | [optional] 
**division_template** | **str** | Division Template | [optional] 
**insurance_sets** | **str** | Insurance Sets | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_company_vendor_insurances_errors_inner import ArrayOfCompanyVendorInsurancesErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCompanyVendorInsurancesErrorsInner from a JSON string
array_of_company_vendor_insurances_errors_inner_instance = ArrayOfCompanyVendorInsurancesErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfCompanyVendorInsurancesErrorsInner.to_json())

# convert the object into a dict
array_of_company_vendor_insurances_errors_inner_dict = array_of_company_vendor_insurances_errors_inner_instance.to_dict()
# create an instance of ArrayOfCompanyVendorInsurancesErrorsInner from a dict
array_of_company_vendor_insurances_errors_inner_from_dict = ArrayOfCompanyVendorInsurancesErrorsInner.from_dict(array_of_company_vendor_insurances_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


