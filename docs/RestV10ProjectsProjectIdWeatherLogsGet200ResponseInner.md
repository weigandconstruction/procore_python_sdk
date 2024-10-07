# RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be depricated, use :name | [optional] 
**average** | **str** | Average temperature for the workday | [optional] 
**calamity** | **str** | Type of calamity the jobsite was subject to | [optional] 
**comments** | **str** | Additional comments | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**is_weather_delay** | **str** | Weather delay status | [optional] 
**ground** | **str** | Ground condition | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**precipitation** | **str** | Precipitation conditions | [optional] 
**sky** | **str** | Sky condition | [optional] 
**temperature** | **str** | Weather temperature | [optional] 
**time** | **datetime** | UTC time weather conditions were observed | [optional] 
**wind** | **str** | Wind condition | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_get200_response_inner import RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_weather_logs_get200_response_inner_instance = RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_weather_logs_get200_response_inner_dict = rest_v10_projects_project_id_weather_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_weather_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_weather_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


