# ProjectAssignmentNormalView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | [optional] 
**name** | **str** | Project name | [optional] 
**project_number** | **str** | Project number | [optional] 
**address** | **str** | Project address | [optional] 
**stage** | **str** | Stage name | [optional] 
**is_assigned** | **bool** | Whether user is assigned to project or not | [optional] 
**active** | **bool** | Whether the project is active or not | [optional] 
**roles** | **List[str]** | Array of user project role names | [optional] 
**permission_template_name** | **str** | Project currently assigned user permission template name | [optional] 
**region** | **str** | Region assigned to the project | [optional] 
**program** | **str** | Program assigned to the project | [optional] 
**project_type** | **str** | Project type assigned to the project | [optional] 

## Example

```python
from procore_sdk.models.project_assignment_normal_view import ProjectAssignmentNormalView

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAssignmentNormalView from a JSON string
project_assignment_normal_view_instance = ProjectAssignmentNormalView.from_json(json)
# print the JSON string representation of the object
print(ProjectAssignmentNormalView.to_json())

# convert the object into a dict
project_assignment_normal_view_dict = project_assignment_normal_view_instance.to_dict()
# create an instance of ProjectAssignmentNormalView from a dict
project_assignment_normal_view_from_dict = ProjectAssignmentNormalView.from_dict(project_assignment_normal_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


