# RestV10ProjectsProjectIdProductivityLogsPostRequestProductivityLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**line_item_id** | **int** | Line Item ID of an approved contract | 
**notes** | **str** | Notes | [optional] 
**quantity_delivered** | **str** | Total number of materials delivered | [optional] 
**quantity_used** | **str** | Total number of materials used | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_post_request_productivity_log import RestV10ProjectsProjectIdProductivityLogsPostRequestProductivityLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdProductivityLogsPostRequestProductivityLog from a JSON string
rest_v10_projects_project_id_productivity_logs_post_request_productivity_log_instance = RestV10ProjectsProjectIdProductivityLogsPostRequestProductivityLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdProductivityLogsPostRequestProductivityLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_productivity_logs_post_request_productivity_log_dict = rest_v10_projects_project_id_productivity_logs_post_request_productivity_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdProductivityLogsPostRequestProductivityLog from a dict
rest_v10_projects_project_id_productivity_logs_post_request_productivity_log_from_dict = RestV10ProjectsProjectIdProductivityLogsPostRequestProductivityLog.from_dict(rest_v10_projects_project_id_productivity_logs_post_request_productivity_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


