# RestV10ProjectsProjectIdSafetyViolationLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**comments** | **str** | Comments | [optional] 
**compliance_due** | **date** | The date the compliance for the safety violation is due by | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**issued_to** | **str** | Person who the safety violation was issued to | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**safety_notice** | **str** | Name/number of the safety notice issued | [optional] 
**subject** | **str** | Reason for the safety violation | [optional] 
**time_hour** | **int** | Time of safety violation - hour | [optional] 
**time_minute** | **int** | Time of safety violation - minute | [optional] 
**var_date** | **date** | 2016-04-19 | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_safety_violation_logs_get200_response_inner import RestV10ProjectsProjectIdSafetyViolationLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSafetyViolationLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_safety_violation_logs_get200_response_inner_instance = RestV10ProjectsProjectIdSafetyViolationLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSafetyViolationLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_safety_violation_logs_get200_response_inner_dict = rest_v10_projects_project_id_safety_violation_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSafetyViolationLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_safety_violation_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdSafetyViolationLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_safety_violation_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


