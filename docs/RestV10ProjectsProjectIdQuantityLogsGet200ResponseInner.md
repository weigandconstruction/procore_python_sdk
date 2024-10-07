# RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**quantity** | **int** | Total number of the specified materials placed on the site that day | [optional] 
**unit** | **str** | Units that were delivered | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | Quantity Log Attachments | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_quantity_logs_get200_response_inner import RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_quantity_logs_get200_response_inner_instance = RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_quantity_logs_get200_response_inner_dict = rest_v10_projects_project_id_quantity_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_quantity_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdQuantityLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_quantity_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


