# RestV10ProjectsProjectIdDumpsterLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**comments** | **str** | Additional comments | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date of record | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**quantity_delivered** | **int** | Number of dumpsters delivered on site | [optional] 
**quantity_removed** | **int** | Number of dumpsters removed from site | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**vendor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | Dumpster Log Attachments are not viewable or used on web | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_dumpster_logs_get200_response_inner import RestV10ProjectsProjectIdDumpsterLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDumpsterLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_dumpster_logs_get200_response_inner_instance = RestV10ProjectsProjectIdDumpsterLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDumpsterLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_dumpster_logs_get200_response_inner_dict = rest_v10_projects_project_id_dumpster_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDumpsterLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_dumpster_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdDumpsterLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_dumpster_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


