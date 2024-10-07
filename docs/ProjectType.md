# ProjectType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Type ID | [optional] 
**name** | **str** | Project Type name | [optional] 

## Example

```python
from procore_sdk.models.project_type import ProjectType

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectType from a JSON string
project_type_instance = ProjectType.from_json(json)
# print the JSON string representation of the object
print(ProjectType.to_json())

# convert the object into a dict
project_type_dict = project_type_instance.to_dict()
# create an instance of ProjectType from a dict
project_type_from_dict = ProjectType.from_dict(project_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


