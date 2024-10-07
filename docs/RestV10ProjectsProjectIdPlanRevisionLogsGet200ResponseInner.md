# RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**category** | **str** | Category of discipline that appears on the revision | [optional] 
**comments** | **str** | Additional comments | [optional] 
**var_date** | **date** | Date of record | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**plan_number** | **str** | Number that appears on the plan submitted | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**revision** | **str** | Revision number | [optional] 
**title** | **str** | Title of the plans | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | Plan Revision Log Attachments are not viewable or used on web | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_plan_revision_logs_get200_response_inner import RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_plan_revision_logs_get200_response_inner_instance = RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_plan_revision_logs_get200_response_inner_dict = rest_v10_projects_project_id_plan_revision_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_plan_revision_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdPlanRevisionLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_plan_revision_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


