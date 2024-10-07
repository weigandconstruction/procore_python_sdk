# RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseSkyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Value used as weather state ID and stored on server | [optional] 
**value** | **str** | Weather state value localized in user&#39;s locale. Intended to be shown for user in UI. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_sky_inner import RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseSkyInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseSkyInner from a JSON string
rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_sky_inner_instance = RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseSkyInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseSkyInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_sky_inner_dict = rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_sky_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseSkyInner from a dict
rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_sky_inner_from_dict = RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseSkyInner.from_dict(rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_sky_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


