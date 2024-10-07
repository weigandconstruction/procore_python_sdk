# RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_emails** | **str** | Parameter to send email to assignees, distribution members and creator of the Punch Item. Parameter must be true and status or comment must have changed for an email to send. | [optional] 
**punch_item_assignment** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequestPunchItemAssignment**](RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequestPunchItemAssignment.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_punch_item_assignments_id_patch_request import RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest from a JSON string
rest_v10_projects_project_id_punch_item_assignments_id_patch_request_instance = RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_punch_item_assignments_id_patch_request_dict = rest_v10_projects_project_id_punch_item_assignments_id_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest from a dict
rest_v10_projects_project_id_punch_item_assignments_id_patch_request_from_dict = RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest.from_dict(rest_v10_projects_project_id_punch_item_assignments_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


