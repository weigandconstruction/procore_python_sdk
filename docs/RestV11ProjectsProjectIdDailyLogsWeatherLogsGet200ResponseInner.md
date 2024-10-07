# RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner

Weather Log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**attachments** | [**List[RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner]**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**average** | **str** | Average temperature for the workday | [optional] 
**calamity** | **str** | Translated Calamity condition based on user&#39;s locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version&#x3D;1.0 | [optional] 
**comments** | **str** | Additional comments | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**is_weather_delay** | **str** | Weather delay status | [optional] 
**ground** | **str** | Translated Ground condition based on user&#39;s locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version&#x3D;1.0 | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**precipitation** | **str** | Precipitation conditions | [optional] 
**sky** | **str** | Translated Sky condition based on user&#39;s locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version&#x3D;1.0 | [optional] 
**temperature** | **str** | Translated Temperature condition based on user&#39;s locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version&#x3D;1.0 | [optional] 
**time** | **datetime** | UTC time weather conditions were observed | [optional] 
**wind** | **str** | Translated Wind condition based on user&#39;s locale. List of possible values can be retrieved using Weather Conditions API https://developers.procore.com/reference/rest/v1/weather-conditions?version&#x3D;1.0 | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner import RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner from a JSON string
rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner_instance = RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner_dict = rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner from a dict
rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner_from_dict = RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner.from_dict(rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


