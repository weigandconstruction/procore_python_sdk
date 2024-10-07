# RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequestRequestedChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Requested Change ID | [optional] 
**approved** | **bool** | Review result | [optional] 
**disposition_reason** | **str** | reason of review | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_requested_changes_inner import RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequestRequestedChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequestRequestedChangesInner from a JSON string
rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_requested_changes_inner_instance = RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequestRequestedChangesInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequestRequestedChangesInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_requested_changes_inner_dict = rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_requested_changes_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequestRequestedChangesInner from a dict
rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_requested_changes_inner_from_dict = RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequestRequestedChangesInner.from_dict(rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_requested_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


