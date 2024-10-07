# RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner

Delay Log Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**display_name** | **str** | The name displayed in the web UI | [optional] 
**translation_key** | **str** | The key used to translate default delay log types | [optional] 
**visible** | **bool** | Whether the type is visible in the UI | [optional] 
**created_at** | **datetime** | The UTC datetime for the creation of the resource in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | The UTC datetime for the last update of the resource in ISO 8601 format. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_delay_log_types_get200_response_inner import RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_daily_logs_delay_log_types_get200_response_inner_instance = RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_logs_delay_log_types_get200_response_inner_dict = rest_v10_projects_project_id_daily_logs_delay_log_types_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner from a dict
rest_v10_projects_project_id_daily_logs_delay_log_types_get200_response_inner_from_dict = RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner.from_dict(rest_v10_projects_project_id_daily_logs_delay_log_types_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


