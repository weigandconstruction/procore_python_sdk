# RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sky** | **List[str]** |  | [optional] 
**ground** | **List[str]** |  | [optional] 
**calamity** | **List[str]** |  | [optional] 
**wind** | **List[str]** |  | [optional] 
**temperature** | **List[str]** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_conditions_get200_response import RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response from a JSON string
rest_v10_projects_project_id_weather_logs_conditions_get200_response_instance = RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_weather_logs_conditions_get200_response_dict = rest_v10_projects_project_id_weather_logs_conditions_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response from a dict
rest_v10_projects_project_id_weather_logs_conditions_get200_response_from_dict = RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response.from_dict(rest_v10_projects_project_id_weather_logs_conditions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


