# RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Requested change id | [optional] 
**requested_by** | **str** | Requested change requested by | [optional] 
**change_requested** | **str** | Requested change | [optional] 
**reason** | **str** | Requested change reason | [optional] 
**status** | **str** | Requested change status localized | [optional] 
**status_not_localized** | **str** | Requested change status not localized | [optional] 
**notes** | **str** | Requested change notes | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_schedule_requested_changes_review_patch200_response_inner import RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner from a JSON string
rest_v11_projects_project_id_schedule_requested_changes_review_patch200_response_inner_instance = RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_schedule_requested_changes_review_patch200_response_inner_dict = rest_v11_projects_project_id_schedule_requested_changes_review_patch200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner from a dict
rest_v11_projects_project_id_schedule_requested_changes_review_patch200_response_inner_from_dict = RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner.from_dict(rest_v11_projects_project_id_schedule_requested_changes_review_patch200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


