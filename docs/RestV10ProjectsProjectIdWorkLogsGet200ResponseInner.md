# RestV10ProjectsProjectIdWorkLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**comments** | **str** | Comments | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**hourly_rate** | **float** | Scheduled work hourly rate | [optional] 
**hours** | **float** | Scheduled work hours | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**reimbursable** | **bool** | If scheduled work is reimbursable | [optional] 
**resource_name** | **str** | Name of the resource associated with the scheduled work | [optional] 
**showed** | **bool** | If scheduled worker kept the work log schedule | [optional] 
**workers** | **int** | Scheduled number of workers | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | Work Log Attachments are not viewable or used on web | [optional] 
**scheduled_tasks** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerScheduledTasksInner]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerScheduledTasksInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner import RestV10ProjectsProjectIdWorkLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWorkLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_work_logs_get200_response_inner_instance = RestV10ProjectsProjectIdWorkLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWorkLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_work_logs_get200_response_inner_dict = rest_v10_projects_project_id_work_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWorkLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_work_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdWorkLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_work_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


