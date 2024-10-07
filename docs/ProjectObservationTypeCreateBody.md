# ProjectObservationTypeCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**observation_type** | [**ProjectObservationType1**](ProjectObservationType1.md) |  | 

## Example

```python
from procore_sdk.models.project_observation_type_create_body import ProjectObservationTypeCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectObservationTypeCreateBody from a JSON string
project_observation_type_create_body_instance = ProjectObservationTypeCreateBody.from_json(json)
# print the JSON string representation of the object
print(ProjectObservationTypeCreateBody.to_json())

# convert the object into a dict
project_observation_type_create_body_dict = project_observation_type_create_body_instance.to_dict()
# create an instance of ProjectObservationTypeCreateBody from a dict
project_observation_type_create_body_from_dict = ProjectObservationTypeCreateBody.from_dict(project_observation_type_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


