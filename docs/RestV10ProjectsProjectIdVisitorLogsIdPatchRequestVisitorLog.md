# RestV10ProjectsProjectIdVisitorLogsIdPatchRequestVisitorLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin_hour** | **int** | Time of visitation - hour | [optional] 
**begin_minute** | **int** | Time of visitation - hour | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**details** | **str** | Details of visit | [optional] 
**end_hour** | **int** | Time that the visitation ended - hour | [optional] 
**end_minute** | **int** | Time that the visitation ended - minute | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_id_patch_request_visitor_log import RestV10ProjectsProjectIdVisitorLogsIdPatchRequestVisitorLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdVisitorLogsIdPatchRequestVisitorLog from a JSON string
rest_v10_projects_project_id_visitor_logs_id_patch_request_visitor_log_instance = RestV10ProjectsProjectIdVisitorLogsIdPatchRequestVisitorLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdVisitorLogsIdPatchRequestVisitorLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_visitor_logs_id_patch_request_visitor_log_dict = rest_v10_projects_project_id_visitor_logs_id_patch_request_visitor_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdVisitorLogsIdPatchRequestVisitorLog from a dict
rest_v10_projects_project_id_visitor_logs_id_patch_request_visitor_log_from_dict = RestV10ProjectsProjectIdVisitorLogsIdPatchRequestVisitorLog.from_dict(rest_v10_projects_project_id_visitor_logs_id_patch_request_visitor_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


