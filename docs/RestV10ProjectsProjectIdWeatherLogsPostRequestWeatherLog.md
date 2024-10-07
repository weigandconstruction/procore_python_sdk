# RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | 
**is_weather_delay** | **int** | Weather delay status | [optional] 
**sky** | **str** | Sky condition - \&quot;\&quot;, \&quot;Clear\&quot;, \&quot;Cloudy\&quot;, \&quot;Overcast\&quot;, \&quot;Fog\&quot;, \&quot;Mist\&quot;, \&quot;Rain\&quot;, \&quot;Snow\&quot;, \&quot;Ice/Sleet/Hail\&quot; | [optional] 
**temperature** | **str** | Weather temperature - \&quot;\&quot;, \&quot;Very Hot\&quot;, \&quot;Hot\&quot;, \&quot;Mild\&quot;, \&quot;Cold\&quot;, \&quot;Very Cold\&quot; | [optional] 
**average** | **str** | Average temperature for the workday | [optional] 
**wind** | **str** | Wind condition - \&quot;\&quot;, \&quot;Calm\&quot;, \&quot;Light Wind\&quot;, \&quot;High Wind\&quot; | [optional] 
**ground** | **str** | Ground condition - \&quot;\&quot;, \&quot;Dry\&quot;, \&quot;Wet/Muddy\&quot;, \&quot;Flooded\&quot;,\&quot;Snow\&quot;,\&quot;Frozen\&quot;,\&quot;-----\&quot;,\&quot;High Tide\&quot;,\&quot;Low Tide\&quot;, \&quot;Heavy Surf/Swell\&quot; | [optional] 
**calamity** | **str** | Type of calamity the jobsite was subject to - \&quot;\&quot;, \&quot;Earthquake\&quot;, \&quot;Fire\&quot;, \&quot;Flash Flood\&quot;, \&quot;Landslide\&quot;, \&quot;Tornado\&quot;, \&quot;Hurricane\&quot;, \&quot;Snow\&quot;,\&quot;Other\&quot; | [optional] 
**precipitation** | **str** | Precipitation conditions | [optional] 
**comments** | **str** | Additional comments | [optional] 
**time** | **str** | UTC time weather conditions were observed. The date of observation must match entry&#39;s date. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_post_request_weather_log import RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog from a JSON string
rest_v10_projects_project_id_weather_logs_post_request_weather_log_instance = RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_weather_logs_post_request_weather_log_dict = rest_v10_projects_project_id_weather_logs_post_request_weather_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog from a dict
rest_v10_projects_project_id_weather_logs_post_request_weather_log_from_dict = RestV10ProjectsProjectIdWeatherLogsPostRequestWeatherLog.from_dict(rest_v10_projects_project_id_weather_logs_post_request_weather_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


