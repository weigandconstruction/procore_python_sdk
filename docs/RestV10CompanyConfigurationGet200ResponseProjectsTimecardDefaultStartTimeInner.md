# RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | ID of the project | [optional] 
**timecard_default_start_time** | **str** | Timecard default start time in format HH:MM | [optional] [default to '8:00']

## Example

```python
from procore_sdk.models.rest_v10_company_configuration_get200_response_projects_timecard_default_start_time_inner import RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner from a JSON string
rest_v10_company_configuration_get200_response_projects_timecard_default_start_time_inner_instance = RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner.to_json())

# convert the object into a dict
rest_v10_company_configuration_get200_response_projects_timecard_default_start_time_inner_dict = rest_v10_company_configuration_get200_response_projects_timecard_default_start_time_inner_instance.to_dict()
# create an instance of RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner from a dict
rest_v10_company_configuration_get200_response_projects_timecard_default_start_time_inner_from_dict = RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner.from_dict(rest_v10_company_configuration_get200_response_projects_timecard_default_start_time_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


