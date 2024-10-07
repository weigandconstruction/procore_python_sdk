# RestV10ProjectsProjectIdDailyLogHeadersGet200Response

A daily log header

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the daily log header | [optional] 
**log_date** | **date** | Date that this daily log header represents Format: YYYY-MM-DD Example: 2016-05-19 | [optional] 
**log_datetime** | **datetime** | Estimated UTC datetime that this daily log header represents | [optional] 
**completed** | **bool** | Is this log date marked as complete? | [optional] 
**completed_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**completed_at** | **datetime** | Daily log header marked complete at | [optional] 
**completable** | **bool** | Is this log date able to be completed? | [optional] 
**distributed** | **bool** | Is this log date marked as distributed? | [optional] 
**distributed_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**distributed_at** | **datetime** | Daily log header marked distributed at | [optional] 
**distributable** | **bool** | Is this log date able to be distributed? | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_log_headers_get200_response import RestV10ProjectsProjectIdDailyLogHeadersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogHeadersGet200Response from a JSON string
rest_v10_projects_project_id_daily_log_headers_get200_response_instance = RestV10ProjectsProjectIdDailyLogHeadersGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogHeadersGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_log_headers_get200_response_dict = rest_v10_projects_project_id_daily_log_headers_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogHeadersGet200Response from a dict
rest_v10_projects_project_id_daily_log_headers_get200_response_from_dict = RestV10ProjectsProjectIdDailyLogHeadersGet200Response.from_dict(rest_v10_projects_project_id_daily_log_headers_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


