# ProjectDepartment1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Project Department | [optional] 
**name** | **str** | The name for the Project Department | [optional] 

## Example

```python
from procore_sdk.models.project_department1 import ProjectDepartment1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDepartment1 from a JSON string
project_department1_instance = ProjectDepartment1.from_json(json)
# print the JSON string representation of the object
print(ProjectDepartment1.to_json())

# convert the object into a dict
project_department1_dict = project_department1_instance.to_dict()
# create an instance of ProjectDepartment1 from a dict
project_department1_from_dict = ProjectDepartment1.from_dict(project_department1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


