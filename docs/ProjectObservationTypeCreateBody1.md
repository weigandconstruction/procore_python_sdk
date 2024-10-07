# ProjectObservationTypeCreateBody1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**observation_type** | [**ProjectObservationType2**](ProjectObservationType2.md) |  | 

## Example

```python
from procore_sdk.models.project_observation_type_create_body1 import ProjectObservationTypeCreateBody1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectObservationTypeCreateBody1 from a JSON string
project_observation_type_create_body1_instance = ProjectObservationTypeCreateBody1.from_json(json)
# print the JSON string representation of the object
print(ProjectObservationTypeCreateBody1.to_json())

# convert the object into a dict
project_observation_type_create_body1_dict = project_observation_type_create_body1_instance.to_dict()
# create an instance of ProjectObservationTypeCreateBody1 from a dict
project_observation_type_create_body1_from_dict = ProjectObservationTypeCreateBody1.from_dict(project_observation_type_create_body1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


