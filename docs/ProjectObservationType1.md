# ProjectObservationType1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name to be used for Observations created from this type. | [optional] 
**category** | **str** | Category to be used for Observations created from this type. | [optional] 
**active** | **bool** | Active or no. | [optional] 
**parent_id** | **int** | Parent id | [optional] 

## Example

```python
from procore_sdk.models.project_observation_type1 import ProjectObservationType1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectObservationType1 from a JSON string
project_observation_type1_instance = ProjectObservationType1.from_json(json)
# print the JSON string representation of the object
print(ProjectObservationType1.to_json())

# convert the object into a dict
project_observation_type1_dict = project_observation_type1_instance.to_dict()
# create an instance of ProjectObservationType1 from a dict
project_observation_type1_from_dict = ProjectObservationType1.from_dict(project_observation_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


