# RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner

Workflow Permanent Log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**activity** | **str** | Name of the activity logged | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**ball_in_court_duration** | **str** | How long the assignee was responsible prior to acting | [optional] 
**comments** | **str** | Comments provided by the assignee when acting in the workflow | [optional] 
**created_at** | **datetime** | Log recorded at | [optional] 
**performed_by** | **str** | Name of the user performing the activity | [optional] 
**user_role** | **str** | Name of the workflow role | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_instance = RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_dict = rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner from a dict
rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_from_dict = RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner.from_dict(rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


