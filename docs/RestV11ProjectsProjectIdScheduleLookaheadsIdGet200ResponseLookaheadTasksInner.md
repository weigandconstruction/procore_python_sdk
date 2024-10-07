# RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner

Schedule Lookahead Task, with subtasks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Lookahead Task ID | [optional] 
**parent_id** | **int** |  | [optional] 
**name** | **str** | Task name | [optional] 
**row_number** | **int** | Number of the task row within the project schedule | [optional] 
**critical_path** | **bool** | Whether or not the task is included in critical path | [optional] 
**comment** | **str** | Additional comments | [optional] 
**activity_id** | **str** | Activity ID | [optional] 
**wbs** | **str** | WBS | [optional] 
**segments** | [**List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerSegmentsInner]**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerSegmentsInner.md) | Segments define the set of days for the entire date range of the task, and the completion status of each day in the task | [optional] 
**resources** | [**List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner]**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner.md) | Resource(s) assigned to this Lookahead Task | [optional] 
**assignees** | [**List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerAssigneesInner]**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerAssigneesInner.md) | Contact(s) assigned to this Lookahead Task | [optional] 
**vendors** | [**List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerVendorsInner]**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerVendorsInner.md) | Company(s) assigned to this Lookahead Task | [optional] 
**task** | [**RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerTask**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerTask.md) |  | [optional] 
**subtasks** | [**List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerSubtasksInner]**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerSubtasksInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner import RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner from a JSON string
rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_instance = RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_dict = rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner from a dict
rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_from_dict = RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner.from_dict(rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


