# RestV10ProjectsProjectIdNotesLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**comment** | **str** | Additional comments | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date of record | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**daily_log_header_id** | **int** | Daily Log Header ID | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**is_issue_day** | **bool** | The note being added is an issue affecting the projet | [optional] 
**permissions** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions.md) |  | [optional] 
**position** | **int** | Order in which this entry was recorded | [optional] 
**status** | **str** | Is a log pending or approved | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**created_by_collaborator** | **bool** |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**location** | [**Location2**](Location2.md) |  | [optional] 
**attachments** | [**List[RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner]**](RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_get200_response_inner import RestV10ProjectsProjectIdNotesLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdNotesLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_notes_logs_get200_response_inner_instance = RestV10ProjectsProjectIdNotesLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdNotesLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_notes_logs_get200_response_inner_dict = rest_v10_projects_project_id_notes_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdNotesLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_notes_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdNotesLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_notes_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


