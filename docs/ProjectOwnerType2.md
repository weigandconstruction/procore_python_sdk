# ProjectOwnerType2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Owner Type ID | [optional] 
**name** | **str** | Project Owner Type name | [optional] 

## Example

```python
from procore_sdk.models.project_owner_type2 import ProjectOwnerType2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectOwnerType2 from a JSON string
project_owner_type2_instance = ProjectOwnerType2.from_json(json)
# print the JSON string representation of the object
print(ProjectOwnerType2.to_json())

# convert the object into a dict
project_owner_type2_dict = project_owner_type2_instance.to_dict()
# create an instance of ProjectOwnerType2 from a dict
project_owner_type2_from_dict = ProjectOwnerType2.from_dict(project_owner_type2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


