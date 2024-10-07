# RestV10ProjectsProjectIdCallLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date that the call took place | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**subject_to** | **str** | Name of the person that received the call | [optional] 
**subject_from** | **str** | Name of the person that called | [optional] 
**description** | **str** | Details describing the call | [optional] 
**start_hour** | **int** | Time when the call started - hour | [optional] 
**start_minute** | **int** | Time when the call started - minute | [optional] 
**end_hour** | **int** | Time when the call ended - hour | [optional] 
**end_minute** | **int** | Time when the call ended - minute | [optional] 
**permissions** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions.md) |  | [optional] 
**position** | **int** | Position in the list of recorded calls for the day | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner]**](RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_call_logs_get200_response_inner import RestV10ProjectsProjectIdCallLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdCallLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_call_logs_get200_response_inner_instance = RestV10ProjectsProjectIdCallLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdCallLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_call_logs_get200_response_inner_dict = rest_v10_projects_project_id_call_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdCallLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_call_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdCallLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_call_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


