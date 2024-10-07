# RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequestRequestedChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_reason** | **str** | Requested change reason | [optional] 
**other_change** | **str** |  | [optional] 
**task** | [**RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequestRequestedChangeTask**](RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequestRequestedChangeTask.md) |  | [optional] 
**notes** | **str** | Requested change notes | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request_requested_change import RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequestRequestedChange

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequestRequestedChange from a JSON string
rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request_requested_change_instance = RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequestRequestedChange.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequestRequestedChange.to_json())

# convert the object into a dict
rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request_requested_change_dict = rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request_requested_change_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequestRequestedChange from a dict
rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request_requested_change_from_dict = RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequestRequestedChange.from_dict(rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request_requested_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


