# ProjectDepartment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Department ID | [optional] 
**name** | **str** | Department name | [optional] 

## Example

```python
from procore_sdk.models.project_department import ProjectDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDepartment from a JSON string
project_department_instance = ProjectDepartment.from_json(json)
# print the JSON string representation of the object
print(ProjectDepartment.to_json())

# convert the object into a dict
project_department_dict = project_department_instance.to_dict()
# create an instance of ProjectDepartment from a dict
project_department_from_dict = ProjectDepartment.from_dict(project_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


