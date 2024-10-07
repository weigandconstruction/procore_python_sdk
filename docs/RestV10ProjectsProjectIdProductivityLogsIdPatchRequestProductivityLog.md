# RestV10ProjectsProjectIdProductivityLogsIdPatchRequestProductivityLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**line_item_id** | **int** | Line Item ID of an approved contract | [optional] 
**notes** | **str** | Notes | [optional] 
**quantity_delivered** | **str** | Total number of materials delivered | [optional] 
**quantity_used** | **str** | Total number of materials used | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_id_patch_request_productivity_log import RestV10ProjectsProjectIdProductivityLogsIdPatchRequestProductivityLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdProductivityLogsIdPatchRequestProductivityLog from a JSON string
rest_v10_projects_project_id_productivity_logs_id_patch_request_productivity_log_instance = RestV10ProjectsProjectIdProductivityLogsIdPatchRequestProductivityLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdProductivityLogsIdPatchRequestProductivityLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_productivity_logs_id_patch_request_productivity_log_dict = rest_v10_projects_project_id_productivity_logs_id_patch_request_productivity_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdProductivityLogsIdPatchRequestProductivityLog from a dict
rest_v10_projects_project_id_productivity_logs_id_patch_request_productivity_log_from_dict = RestV10ProjectsProjectIdProductivityLogsIdPatchRequestProductivityLog.from_dict(rest_v10_projects_project_id_productivity_logs_id_patch_request_productivity_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


