# RestV10ProjectsProjectIdDelayLogsPostRequestDelayLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Additional comments | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**daily_log_header_id** | **int** | Daily Log Header ID | [optional] 
**delay_type** | **str** | Type of delay | [optional] 
**location_id** | **int** | The ID of the Location of the Log. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60; | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 
**start_time** | **str** | Time when the delay started, Format: HH:MM Example: 21:39 | [optional] 
**start_time_hour** | **float** | Number between 0 and 23 representing hour of day | [optional] 
**start_time_minute** | **float** | Number between 0 and 59 representing minute | [optional] 
**end_time** | **str** | Time when the delay started, Format: HH:MM Example: 21:39 | [optional] 
**end_time_hour** | **float** | Number between 0 and 23 representing hour of day | [optional] 
**end_time_minute** | **float** | Number between 0 and 59 representing minute | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_delay_logs_post_request_delay_log import RestV10ProjectsProjectIdDelayLogsPostRequestDelayLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDelayLogsPostRequestDelayLog from a JSON string
rest_v10_projects_project_id_delay_logs_post_request_delay_log_instance = RestV10ProjectsProjectIdDelayLogsPostRequestDelayLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDelayLogsPostRequestDelayLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_delay_logs_post_request_delay_log_dict = rest_v10_projects_project_id_delay_logs_post_request_delay_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDelayLogsPostRequestDelayLog from a dict
rest_v10_projects_project_id_delay_logs_post_request_delay_log_from_dict = RestV10ProjectsProjectIdDelayLogsPostRequestDelayLog.from_dict(rest_v10_projects_project_id_delay_logs_post_request_delay_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


