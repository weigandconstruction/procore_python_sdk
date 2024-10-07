# RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | ID of the project | [optional] 
**timecard_default_stop_time** | **str** | Timecard default stop time in format HH:MM | [optional] [default to '17:00']

## Example

```python
from procore_sdk.models.rest_v10_company_configuration_get200_response_projects_timecard_default_stop_time_inner import RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner from a JSON string
rest_v10_company_configuration_get200_response_projects_timecard_default_stop_time_inner_instance = RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner.to_json())

# convert the object into a dict
rest_v10_company_configuration_get200_response_projects_timecard_default_stop_time_inner_dict = rest_v10_company_configuration_get200_response_projects_timecard_default_stop_time_inner_instance.to_dict()
# create an instance of RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner from a dict
rest_v10_company_configuration_get200_response_projects_timecard_default_stop_time_inner_from_dict = RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner.from_dict(rest_v10_company_configuration_get200_response_projects_timecard_default_stop_time_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


