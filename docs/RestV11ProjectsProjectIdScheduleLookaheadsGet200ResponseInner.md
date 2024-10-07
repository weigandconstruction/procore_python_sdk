# RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner

Schedule Lookahead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Lookahead ID | [optional] 
**start_date** | **datetime** | Lookahead start date, in project time zone | [optional] 
**end_date** | **datetime** | Lookahead end date, in project time zone | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner import RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner from a JSON string
rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner_instance = RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner_dict = rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner from a dict
rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner_from_dict = RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner.from_dict(rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


