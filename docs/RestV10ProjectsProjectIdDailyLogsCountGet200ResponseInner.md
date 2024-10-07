# RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner

Meta data about a daily log module

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_name** | **str** | The name of the log type | [optional] 
**count** | **int** | The number of logs that match the current date and permissions filters for this module | [optional] 
**position** | **int** | The position this module is shown at, on the web | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_count_get200_response_inner import RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner from a JSON string
rest_v10_projects_project_id_daily_logs_count_get200_response_inner_instance = RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_logs_count_get200_response_inner_dict = rest_v10_projects_project_id_daily_logs_count_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner from a dict
rest_v10_projects_project_id_daily_logs_count_get200_response_inner_from_dict = RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner.from_dict(rest_v10_projects_project_id_daily_logs_count_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


