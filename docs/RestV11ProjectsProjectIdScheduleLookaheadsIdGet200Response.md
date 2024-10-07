# RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response

Schedule Lookahead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Lookahead ID | [optional] 
**start_date** | **date** | Lookahead start date, in project time zone | [optional] 
**end_date** | **date** | Lookahead end date, in project time zone | [optional] 
**created_at** | **datetime** | Lookahead creation time | [optional] 
**data_date** | **datetime** | Lookahead last update time | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**label** | **str** | Lookahead label | [optional] 
**lookahead_tasks** | [**List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner]**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInner.md) | List of tasks in the Lookahead, given in a nested tree structure according to parent-child relationships | [optional] 
**generation_errors** | [**List[RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInner]**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInner.md) | List of errors that appeared during Lookahead generation. | [optional] 
**status** | **str** | Lookahead processing status. | [optional] 
**weeks** | **int** | Number of weeks the Lookahead spans in duration | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get200_response import RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response from a JSON string
rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_instance = RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_dict = rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response from a dict
rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_from_dict = RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response.from_dict(rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


