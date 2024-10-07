# RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_changes** | [**List[RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequestRequestedChangesInner]**](RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequestRequestedChangesInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_schedule_requested_changes_review_patch_request import RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest from a JSON string
rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_instance = RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest.to_json())

# convert the object into a dict
rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_dict = rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest from a dict
rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_from_dict = RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest.from_dict(rest_v11_projects_project_id_schedule_requested_changes_review_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


