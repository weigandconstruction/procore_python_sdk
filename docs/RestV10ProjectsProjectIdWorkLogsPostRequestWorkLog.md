# RestV10ProjectsProjectIdWorkLogsPostRequestWorkLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Comments | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**hourly_rate** | **float** | Scheduled work hourly rate | [optional] 
**hours** | **float** | Scheduled work hours | [optional] 
**reimbursable** | **bool** | If scheduled work is reimbursable | [optional] 
**resource_name** | **str** | Resource Name | [optional] 
**showed** | **bool** | If scheduled worker kept the work log schedule | [optional] 
**workers** | **int** | Scheduled number of workers | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_work_logs_post_request_work_log import RestV10ProjectsProjectIdWorkLogsPostRequestWorkLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWorkLogsPostRequestWorkLog from a JSON string
rest_v10_projects_project_id_work_logs_post_request_work_log_instance = RestV10ProjectsProjectIdWorkLogsPostRequestWorkLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWorkLogsPostRequestWorkLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_work_logs_post_request_work_log_dict = rest_v10_projects_project_id_work_logs_post_request_work_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWorkLogsPostRequestWorkLog from a dict
rest_v10_projects_project_id_work_logs_post_request_work_log_from_dict = RestV10ProjectsProjectIdWorkLogsPostRequestWorkLog.from_dict(rest_v10_projects_project_id_work_logs_post_request_work_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


