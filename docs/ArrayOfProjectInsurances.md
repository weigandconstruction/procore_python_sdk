# ArrayOfProjectInsurances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[Insurance]**](Insurance.md) |  | [optional] 
**errors** | [**List[ArrayOfCompanyVendorInsurancesErrorsInner]**](ArrayOfCompanyVendorInsurancesErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_project_insurances import ArrayOfProjectInsurances

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProjectInsurances from a JSON string
array_of_project_insurances_instance = ArrayOfProjectInsurances.from_json(json)
# print the JSON string representation of the object
print(ArrayOfProjectInsurances.to_json())

# convert the object into a dict
array_of_project_insurances_dict = array_of_project_insurances_instance.to_dict()
# create an instance of ArrayOfProjectInsurances from a dict
array_of_project_insurances_from_dict = ArrayOfProjectInsurances.from_dict(array_of_project_insurances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


