# RestV10ProjectsProjectIdDumpsterLogsPostRequestDumpsterLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Additional comments | [optional] 
**var_date** | **date** | Date of record. Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**quantity_delivered** | **int** | Number of dumpsters delivered on | [optional] 
**quantity_removed** | **int** | Number of dumpsters removed from site | [optional] 
**vendor_id** | **int** | Associated Vendor ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_dumpster_logs_post_request_dumpster_log import RestV10ProjectsProjectIdDumpsterLogsPostRequestDumpsterLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDumpsterLogsPostRequestDumpsterLog from a JSON string
rest_v10_projects_project_id_dumpster_logs_post_request_dumpster_log_instance = RestV10ProjectsProjectIdDumpsterLogsPostRequestDumpsterLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDumpsterLogsPostRequestDumpsterLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_dumpster_logs_post_request_dumpster_log_dict = rest_v10_projects_project_id_dumpster_logs_post_request_dumpster_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDumpsterLogsPostRequestDumpsterLog from a dict
rest_v10_projects_project_id_dumpster_logs_post_request_dumpster_log_from_dict = RestV10ProjectsProjectIdDumpsterLogsPostRequestDumpsterLog.from_dict(rest_v10_projects_project_id_dumpster_logs_post_request_dumpster_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


