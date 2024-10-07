# RestV10ProjectsProjectIdInspectionLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**area** | **str** | Area within the specified location | [optional] 
**comments** | **str** | Additional comments | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date of inspection | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**end_hour** | **int** | Ending time of inspection - hour | [optional] 
**end_minute** | **int** | Ending time of inspection - minute | [optional] 
**inspecting_entity** | **str** | Type of inspector performing the inspection | [optional] 
**inspection_type** | **str** | Type of inspection performed | [optional] 
**inspector_name** | **str** | Name of the inspector | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**start_hour** | **int** | Starting time of inspection - hour | [optional] 
**start_minute** | **int** | Starting time of inspection - minute | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_inspection_logs_get200_response_inner import RestV10ProjectsProjectIdInspectionLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdInspectionLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_inspection_logs_get200_response_inner_instance = RestV10ProjectsProjectIdInspectionLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdInspectionLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_inspection_logs_get200_response_inner_dict = rest_v10_projects_project_id_inspection_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdInspectionLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_inspection_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdInspectionLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_inspection_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


