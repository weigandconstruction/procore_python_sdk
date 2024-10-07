# ArrayOfCompanyInsurances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[Insurance]**](Insurance.md) |  | [optional] 
**errors** | [**List[ArrayOfCompanyVendorInsurancesErrorsInner]**](ArrayOfCompanyVendorInsurancesErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_company_insurances import ArrayOfCompanyInsurances

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCompanyInsurances from a JSON string
array_of_company_insurances_instance = ArrayOfCompanyInsurances.from_json(json)
# print the JSON string representation of the object
print(ArrayOfCompanyInsurances.to_json())

# convert the object into a dict
array_of_company_insurances_dict = array_of_company_insurances_instance.to_dict()
# create an instance of ArrayOfCompanyInsurances from a dict
array_of_company_insurances_from_dict = ArrayOfCompanyInsurances.from_dict(array_of_company_insurances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


