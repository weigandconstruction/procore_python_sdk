# RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequestWeatherLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of the Weather Log. Format: YYYY-MM-DD | 
**is_weather_delay** | **int** | Weather delay status | [optional] 
**calamity** | **str** | Type of calamity the jobsite was subject to | [optional] 
**ground** | **str** | Ground condition | [optional] 
**sky** | **str** | Sky condition | [optional] 
**temperature** | **str** | Weather temperature | [optional] 
**wind** | **str** | Wind condition | [optional] 
**average** | **str** | Average temperature for the workday | [optional] 
**precipitation** | **str** | Precipitation conditions | [optional] 
**comments** | **str** | Additional comments | [optional] 
**time** | **str** | UTC time weather conditions were observed. The date of observation must match entry&#39;s date. | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_post_request_weather_log import RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequestWeatherLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequestWeatherLog from a JSON string
rest_v11_projects_project_id_daily_logs_weather_logs_post_request_weather_log_instance = RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequestWeatherLog.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequestWeatherLog.to_json())

# convert the object into a dict
rest_v11_projects_project_id_daily_logs_weather_logs_post_request_weather_log_dict = rest_v11_projects_project_id_daily_logs_weather_logs_post_request_weather_log_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequestWeatherLog from a dict
rest_v11_projects_project_id_daily_logs_weather_logs_post_request_weather_log_from_dict = RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequestWeatherLog.from_dict(rest_v11_projects_project_id_daily_logs_weather_logs_post_request_weather_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


