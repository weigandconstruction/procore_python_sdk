# RestV10ProjectsProjectIdCallLogsPostRequestCallLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date that the call took place. Format: YYYY-MM-DD Example: 2016-05-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**description** | **str** | Description | [optional] 
**end_hour** | **int** | Time when the call ended - hour | [optional] [default to 0]
**end_minute** | **int** | Time when the call ended - minute | [optional] [default to 0]
**start_hour** | **int** | Time when the call started - hour | [optional] [default to 0]
**start_minute** | **int** | Time when the call started - minute | [optional] [default to 0]
**subject_from** | **str** | Name of the person that called | [optional] 
**subject_to** | **str** | Name of the person that received the call | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_call_logs_post_request_call_log import RestV10ProjectsProjectIdCallLogsPostRequestCallLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdCallLogsPostRequestCallLog from a JSON string
rest_v10_projects_project_id_call_logs_post_request_call_log_instance = RestV10ProjectsProjectIdCallLogsPostRequestCallLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdCallLogsPostRequestCallLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_call_logs_post_request_call_log_dict = rest_v10_projects_project_id_call_logs_post_request_call_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdCallLogsPostRequestCallLog from a dict
rest_v10_projects_project_id_call_logs_post_request_call_log_from_dict = RestV10ProjectsProjectIdCallLogsPostRequestCallLog.from_dict(rest_v10_projects_project_id_call_logs_post_request_call_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


