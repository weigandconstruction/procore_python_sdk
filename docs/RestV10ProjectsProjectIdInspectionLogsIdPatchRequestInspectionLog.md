# RestV10ProjectsProjectIdInspectionLogsIdPatchRequestInspectionLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** | Area within the specified location | [optional] 
**comments** | **str** | Additional comments | [optional] 
**var_date** | **date** | Date of inspection. Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**end_hour** | **int** | Ending time of inspection - hour | [optional] 
**end_minute** | **int** | Ending time of inspection - minute | [optional] 
**inspecting_entity** | **str** | Type of inspector that performing the inspection | [optional] 
**inspection_type** | **str** | Type of inspection performed | [optional] 
**inspector_name** | **str** | Name of the inspector | [optional] 
**start_hour** | **int** | Starting time of inspection - hour | [optional] 
**start_minute** | **int** | Starting time of inspection - minute | [optional] 
**location_id** | **int** | The ID of the Location of the Inspection Log. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60; | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_inspection_logs_id_patch_request_inspection_log import RestV10ProjectsProjectIdInspectionLogsIdPatchRequestInspectionLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdInspectionLogsIdPatchRequestInspectionLog from a JSON string
rest_v10_projects_project_id_inspection_logs_id_patch_request_inspection_log_instance = RestV10ProjectsProjectIdInspectionLogsIdPatchRequestInspectionLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdInspectionLogsIdPatchRequestInspectionLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_inspection_logs_id_patch_request_inspection_log_dict = rest_v10_projects_project_id_inspection_logs_id_patch_request_inspection_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdInspectionLogsIdPatchRequestInspectionLog from a dict
rest_v10_projects_project_id_inspection_logs_id_patch_request_inspection_log_from_dict = RestV10ProjectsProjectIdInspectionLogsIdPatchRequestInspectionLog.from_dict(rest_v10_projects_project_id_inspection_logs_id_patch_request_inspection_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


