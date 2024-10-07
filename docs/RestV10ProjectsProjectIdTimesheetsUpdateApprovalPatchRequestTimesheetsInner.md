# RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequestTimesheetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of Timesheet to change the status of | [optional] 
**status** | **str** | The status of the Timesheet - pending/approved | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_timesheets_update_approval_patch_request_timesheets_inner import RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequestTimesheetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequestTimesheetsInner from a JSON string
rest_v10_projects_project_id_timesheets_update_approval_patch_request_timesheets_inner_instance = RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequestTimesheetsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequestTimesheetsInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_timesheets_update_approval_patch_request_timesheets_inner_dict = rest_v10_projects_project_id_timesheets_update_approval_patch_request_timesheets_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequestTimesheetsInner from a dict
rest_v10_projects_project_id_timesheets_update_approval_patch_request_timesheets_inner_from_dict = RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequestTimesheetsInner.from_dict(rest_v10_projects_project_id_timesheets_update_approval_patch_request_timesheets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


