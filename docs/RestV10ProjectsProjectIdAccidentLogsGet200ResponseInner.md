# RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**comments** | **str** | Additional information about the accident | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date that the accident occurred | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**involved_name** | **str** | Name of the person involved in the accident | [optional] 
**permissions** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions.md) |  | [optional] 
**involved_company** | **str** | Name of the Company involved in the accident | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**time_hour** | **int** | Time of accident - hour | [optional] 
**time_minute** | **int** | Time of accident - minute | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner]**](RestV10ProjectsProjectIdNotesLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_accident_logs_get200_response_inner import RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_accident_logs_get200_response_inner_instance = RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_accident_logs_get200_response_inner_dict = rest_v10_projects_project_id_accident_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_accident_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_accident_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


