# RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response

Accepted weather conditions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sky** | [**List[RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseSkyInner]**](RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseSkyInner.md) |  | [optional] 
**ground** | [**List[RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseGroundInner]**](RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseGroundInner.md) |  | [optional] 
**calamity** | [**List[RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseCalamityInner]**](RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseCalamityInner.md) |  | [optional] 
**wind** | [**List[RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseWindInner]**](RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseWindInner.md) |  | [optional] 
**temperature** | [**List[RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseTemperatureInner]**](RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200ResponseTemperatureInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response import RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response from a JSON string
rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_instance = RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_dict = rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response from a dict
rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_from_dict = RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response.from_dict(rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


