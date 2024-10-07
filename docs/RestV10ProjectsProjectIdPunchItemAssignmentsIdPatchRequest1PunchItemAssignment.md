# RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest1PunchItemAssignment

Punch Item Assignment object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | Resolution status | [optional] [default to False]
**comment** | **str** | Comment | [optional] 
**login_information_id** | **int** | User ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_punch_item_assignments_id_patch_request1_punch_item_assignment import RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest1PunchItemAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest1PunchItemAssignment from a JSON string
rest_v10_projects_project_id_punch_item_assignments_id_patch_request1_punch_item_assignment_instance = RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest1PunchItemAssignment.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest1PunchItemAssignment.to_json())

# convert the object into a dict
rest_v10_projects_project_id_punch_item_assignments_id_patch_request1_punch_item_assignment_dict = rest_v10_projects_project_id_punch_item_assignments_id_patch_request1_punch_item_assignment_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest1PunchItemAssignment from a dict
rest_v10_projects_project_id_punch_item_assignments_id_patch_request1_punch_item_assignment_from_dict = RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest1PunchItemAssignment.from_dict(rest_v10_projects_project_id_punch_item_assignments_id_patch_request1_punch_item_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


