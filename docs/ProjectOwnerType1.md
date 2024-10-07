# ProjectOwnerType1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Project Owner Type | [optional] 
**name** | **str** | The name for the Project Owner Type | [optional] 

## Example

```python
from procore_sdk.models.project_owner_type1 import ProjectOwnerType1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectOwnerType1 from a JSON string
project_owner_type1_instance = ProjectOwnerType1.from_json(json)
# print the JSON string representation of the object
print(ProjectOwnerType1.to_json())

# convert the object into a dict
project_owner_type1_dict = project_owner_type1_instance.to_dict()
# create an instance of ProjectOwnerType1 from a dict
project_owner_type1_from_dict = ProjectOwnerType1.from_dict(project_owner_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


