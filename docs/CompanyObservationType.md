# CompanyObservationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Company Observation Type ID | [optional] 
**name** | **str** | Company Observation Type Name | [optional] 
**localized_name** | **str** | Localized name for Company Observation Type | [optional] 
**category** | **str** | Category for Company Observation Type | [optional] 
**category_key** | **str** | category key | [optional] 
**company_active** | **bool** | Flag denoting if the Company Observation Type is available for use | [optional] 
**active** | **bool** | Flag denoting if the Current Observation Type is available for use | [optional] 
**kind** | **str** | Description of whether the Observation Type belongs to a company or project | [optional] 
**parent_inactive** | **bool** | Always false, since Company Observation Types do not have a parent | [optional] 
**in_use** | **bool** | Flag denoting if current Observation Type is in use | [optional] 
**name_translations** | **str** | A translated name for the current Observation Type | [optional] 

## Example

```python
from procore_sdk.models.company_observation_type import CompanyObservationType

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyObservationType from a JSON string
company_observation_type_instance = CompanyObservationType.from_json(json)
# print the JSON string representation of the object
print(CompanyObservationType.to_json())

# convert the object into a dict
company_observation_type_dict = company_observation_type_instance.to_dict()
# create an instance of CompanyObservationType from a dict
company_observation_type_from_dict = CompanyObservationType.from_dict(company_observation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


