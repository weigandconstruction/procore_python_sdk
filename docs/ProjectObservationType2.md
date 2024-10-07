# ProjectObservationType2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name to be used for Observations created from this type. | [optional] 
**category** | **str** | Category to be used for Observations created from this type. | [optional] 
**active** | **bool** | Flag denoting if the Observation Type is available for use. | [optional] 

## Example

```python
from procore_sdk.models.project_observation_type2 import ProjectObservationType2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectObservationType2 from a JSON string
project_observation_type2_instance = ProjectObservationType2.from_json(json)
# print the JSON string representation of the object
print(ProjectObservationType2.to_json())

# convert the object into a dict
project_observation_type2_dict = project_observation_type2_instance.to_dict()
# create an instance of ProjectObservationType2 from a dict
project_observation_type2_from_dict = ProjectObservationType2.from_dict(project_observation_type2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


