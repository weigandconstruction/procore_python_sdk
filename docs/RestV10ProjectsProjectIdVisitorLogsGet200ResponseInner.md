# RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**begin_hour** | **int** | Time of visitation - hour | [optional] 
**begin_minute** | **int** | Time of visitation - hour | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**details** | **str** | Details of visit | [optional] 
**end_hour** | **int** | Time that the visitation ended - hour | [optional] 
**end_minute** | **int** | Time that the visitation ended - minute | [optional] 
**position** | **int** | Order in which this entry was recorded for the day | [optional] 
**status** | **str** | Is a log pending or approved | [optional] 
**subject** | **str** |  | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**permissions** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_visitor_logs_get200_response_inner_instance = RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_visitor_logs_get200_response_inner_dict = rest_v10_projects_project_id_visitor_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_visitor_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_visitor_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


