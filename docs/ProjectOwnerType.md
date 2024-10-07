# ProjectOwnerType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Owner Type ID | [optional] 
**name** | **str** | Project Owner Type name | [optional] 

## Example

```python
from procore_sdk.models.project_owner_type import ProjectOwnerType

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectOwnerType from a JSON string
project_owner_type_instance = ProjectOwnerType.from_json(json)
# print the JSON string representation of the object
print(ProjectOwnerType.to_json())

# convert the object into a dict
project_owner_type_dict = project_owner_type_instance.to_dict()
# create an instance of ProjectOwnerType from a dict
project_owner_type_from_dict = ProjectOwnerType.from_dict(project_owner_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


