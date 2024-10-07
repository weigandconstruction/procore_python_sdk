# CompanyObservationTemplate1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Company Observation Template ID | [optional] 
**observation_title** | **str** | Title to be used for Observations created from this template | [optional] 
**observation_type** | [**CompanyObservationType**](CompanyObservationType.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 

## Example

```python
from procore_sdk.models.company_observation_template1 import CompanyObservationTemplate1

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyObservationTemplate1 from a JSON string
company_observation_template1_instance = CompanyObservationTemplate1.from_json(json)
# print the JSON string representation of the object
print(CompanyObservationTemplate1.to_json())

# convert the object into a dict
company_observation_template1_dict = company_observation_template1_instance.to_dict()
# create an instance of CompanyObservationTemplate1 from a dict
company_observation_template1_from_dict = CompanyObservationTemplate1.from_dict(company_observation_template1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


