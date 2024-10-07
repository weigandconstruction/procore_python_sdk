# ArrayOfCompanyVendorInsurances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[Insurance]**](Insurance.md) |  | [optional] 
**errors** | [**List[ArrayOfCompanyVendorInsurancesErrorsInner]**](ArrayOfCompanyVendorInsurancesErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_company_vendor_insurances import ArrayOfCompanyVendorInsurances

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCompanyVendorInsurances from a JSON string
array_of_company_vendor_insurances_instance = ArrayOfCompanyVendorInsurances.from_json(json)
# print the JSON string representation of the object
print(ArrayOfCompanyVendorInsurances.to_json())

# convert the object into a dict
array_of_company_vendor_insurances_dict = array_of_company_vendor_insurances_instance.to_dict()
# create an instance of ArrayOfCompanyVendorInsurances from a dict
array_of_company_vendor_insurances_from_dict = ArrayOfCompanyVendorInsurances.from_dict(array_of_company_vendor_insurances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


