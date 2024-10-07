# RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_uid** | **str** | The unique identifier for this resource from the external system which owns the schedule data. | [optional] 
**id** | **int** | Resource id | [optional] 
**name** | **str** | Resource name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_resources_inner import RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner from a JSON string
rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_resources_inner_instance = RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_resources_inner_dict = rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_resources_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner from a dict
rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_resources_inner_from_dict = RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner.from_dict(rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


