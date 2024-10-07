# RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timesheets** | [**List[RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequestTimesheetsInner]**](RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequestTimesheetsInner.md) | array of Timesheet objects | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_timesheets_update_approval_patch_request import RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest from a JSON string
rest_v10_projects_project_id_timesheets_update_approval_patch_request_instance = RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_timesheets_update_approval_patch_request_dict = rest_v10_projects_project_id_timesheets_update_approval_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest from a dict
rest_v10_projects_project_id_timesheets_update_approval_patch_request_from_dict = RestV10ProjectsProjectIdTimesheetsUpdateApprovalPatchRequest.from_dict(rest_v10_projects_project_id_timesheets_update_approval_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


