# RestV10ProjectsProjectIdNotesLogsIdPatchRequestNotesLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Additional comments | [optional] 
**var_date** | **date** | Date of record. Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**daily_log_header_id** | **int** | Daily Log Header ID | [optional] 
**is_issue_day** | **bool** | The note being added is an issue affecting the project | [optional] 
**location_id** | **int** | The ID of the Location of the Notes Log. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60; | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 
**status** | **str** | Approval for pending logs | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_id_patch_request_notes_log import RestV10ProjectsProjectIdNotesLogsIdPatchRequestNotesLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdNotesLogsIdPatchRequestNotesLog from a JSON string
rest_v10_projects_project_id_notes_logs_id_patch_request_notes_log_instance = RestV10ProjectsProjectIdNotesLogsIdPatchRequestNotesLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdNotesLogsIdPatchRequestNotesLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_notes_logs_id_patch_request_notes_log_dict = rest_v10_projects_project_id_notes_logs_id_patch_request_notes_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdNotesLogsIdPatchRequestNotesLog from a dict
rest_v10_projects_project_id_notes_logs_id_patch_request_notes_log_from_dict = RestV10ProjectsProjectIdNotesLogsIdPatchRequestNotesLog.from_dict(rest_v10_projects_project_id_notes_logs_id_patch_request_notes_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


