# ProjectObservationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Observation Type ID | [optional] 
**name** | **str** | Project Observation Type Name | [optional] 
**localized_name** | **str** | Localized name for Project Observation Type | [optional] 
**category** | **str** | Category for Project Observation Type | [optional] 
**category_key** | **str** | category key | [optional] 
**name_translations** | **str** | name translations | [optional] 
**active** | **bool** | Flag denoting if the Observation Type is available for use | [optional] 
**company_active** | **bool** | Flag denoting if the Company is available for use | [optional] 
**parent_inactive** | **bool** | Flag denoting if the Parent is available for use | [optional] 
**in_use** | **bool** | Flag denoting if the in use is available for use | [optional] 
**kind** | **str** | kind | [optional] 

## Example

```python
from procore_sdk.models.project_observation_type import ProjectObservationType

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectObservationType from a JSON string
project_observation_type_instance = ProjectObservationType.from_json(json)
# print the JSON string representation of the object
print(ProjectObservationType.to_json())

# convert the object into a dict
project_observation_type_dict = project_observation_type_instance.to_dict()
# create an instance of ProjectObservationType from a dict
project_observation_type_from_dict = ProjectObservationType.from_dict(project_observation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


