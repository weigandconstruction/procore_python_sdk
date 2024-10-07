# RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response

Schedule Lookahead Task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Lookahead Task ID | [optional] 
**project_id** | **int** | ID of the associated Project | [optional] 
**company_id** | **int** | ID of the associated Company | [optional] 
**lookahead_id** | **int** | ID of the associated Lookahead | [optional] 
**task_id** | **int** | ID of the associated Task in the Master Schedule | [optional] 
**created_at** | **datetime** | Lookahead Task creation time | [optional] 
**created_by_id** | **int** | ID of the user who created the Lookahead Task | [optional] 
**parent_id** | **int** | ID of the parent Lookahead Task | [optional] 
**name** | **str** | The name of the Lookahead Task | [optional] 
**start_date** | **str** | Lookahead Task start date, in project time zone | [optional] 
**end_date** | **str** | Lookahead Task end date, in project time zone | [optional] 
**row_number** | **int** | Defines the sequence in which Lookahead Tasks are normally expected to be displayed | [optional] 
**critical_path** | **bool** | True if this Lookahead Task is on the critical path | [optional] 
**comment** | **str** | Additional comments | [optional] 
**activity_id** | **str** | Activity ID | [optional] 
**wbs** | **str** | WBS | [optional] 
**assignee_ids** | **List[int]** | IDs of Assignee(s) assigned to this Lookahead Task | [optional] 
**resource_ids** | **List[int]** | IDs of Resource(s) assigned to this Lookahead Task | [optional] 
**vendor_ids** | **List[int]** | IDs of Vendor(s) assigned to this Lookahead Task | [optional] 
**segments** | [**List[RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseSegmentsInner]**](RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseSegmentsInner.md) | Segments define the set of days for the entire date range of the Lookahead Task, and the completion status of each day in the Lookahead Task | [optional] 
**resources** | [**List[RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner]**](RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner.md) | Resources assigned to this Task | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response import RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response from a JSON string
rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_instance = RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_dict = rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response from a dict
rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_from_dict = RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response.from_dict(rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


