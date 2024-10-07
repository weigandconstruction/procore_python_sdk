# RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_activity_feed** | **bool** |  | [optional] 
**schedule_comment_mentions** | **bool** |  | [optional] 
**schedule_gantt_crud** | **bool** |  | [optional] 
**schedule_task_comments** | **bool** |  | [optional] 
**schedule_task_details** | **bool** |  | [optional] 
**schedule_linked_items** | **bool** |  | [optional] 
**new_princess_enabled** | **bool** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_schedule_get200_response_active_features import RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures from a JSON string
rest_v10_projects_project_id_schedule_get200_response_active_features_instance = RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures.to_json())

# convert the object into a dict
rest_v10_projects_project_id_schedule_get200_response_active_features_dict = rest_v10_projects_project_id_schedule_get200_response_active_features_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures from a dict
rest_v10_projects_project_id_schedule_get200_response_active_features_from_dict = RestV10ProjectsProjectIdScheduleGet200ResponseActiveFeatures.from_dict(rest_v10_projects_project_id_schedule_get200_response_active_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


