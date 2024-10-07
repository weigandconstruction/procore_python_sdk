# RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerTask

The Master Scheduled Task this Lookahead Task corresponds with, if one exists

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Lookahead ID | [optional] 
**finish** | **datetime** | Task finish time | [optional] 
**start** | **datetime** | Task start time | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_task import RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerTask

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerTask from a JSON string
rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_task_instance = RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerTask.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerTask.to_json())

# convert the object into a dict
rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_task_dict = rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_task_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerTask from a dict
rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_task_from_dict = RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerTask.from_dict(rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


