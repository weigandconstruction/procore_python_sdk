# RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Requested change id | [optional] 
**change_requested** | **str** | Requested change | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**new_finish** | **date** | Requested change finish date | [optional] 
**new_start** | **date** | Requested change start date | [optional] 
**new_percentage** | **int** | Requested change percentage | [optional] 
**old_finish** | **date** | Current finish date | [optional] 
**old_start** | **date** | Current start date | [optional] 
**old_percentage** | **int** | Current percentage | [optional] 
**other_change** | **str** | Other change | [optional] 
**reason** | **str** | Requested change reason | [optional] 
**status** | **str** | Localized requested change status | [optional] 
**status_not_localized** | **str** | Requested change status not localized | [optional] 
**notes** | **str** | Requested change notes | [optional] 
**created_at** | **date** | Requested change created date | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_schedule_requested_changes_get200_response_inner import RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner from a JSON string
rest_v11_projects_project_id_schedule_requested_changes_get200_response_inner_instance = RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_schedule_requested_changes_get200_response_inner_dict = rest_v11_projects_project_id_schedule_requested_changes_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner from a dict
rest_v11_projects_project_id_schedule_requested_changes_get200_response_inner_from_dict = RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner.from_dict(rest_v11_projects_project_id_schedule_requested_changes_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


