# RestV10ProjectsProjectIdDelayLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**comments** | **str** | Additional comments | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date of record | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**delay_type** | **str** | Type of delay | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**duration** | **int** | Number of hours the delay lasted (between 1 and 24) | [optional] 
**end_time** | **str** | Time when the delay ended, Format: HH:MM Example: 21:39 | [optional] 
**end_time_hour** | **float** | Number between 0 and 23 representing hour of day | [optional] 
**end_time_minute** | **float** | Number between 0 and 59 representing minute | [optional] 
**position** | **int** | Order in which this entry was recorded | [optional] 
**status** | **str** | Is a log pending or approved | [optional] 
**start_time_hour** | **float** | Number between 0 and 23 representing hour of day | [optional] 
**start_time_minute** | **float** | Number between 0 and 59 representing minute | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_delay_logs_get200_response_inner import RestV10ProjectsProjectIdDelayLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDelayLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_delay_logs_get200_response_inner_instance = RestV10ProjectsProjectIdDelayLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDelayLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_delay_logs_get200_response_inner_dict = rest_v10_projects_project_id_delay_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDelayLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_delay_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdDelayLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_delay_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


