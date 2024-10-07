# RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequestSafetyViolationLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Comments | [optional] 
**compliance_due** | **date** | The date the compliance for the safety violation is due by | [optional] 
**issued_to** | **str** | Person who the safety violation was issued to | [optional] 
**safety_notice** | **str** | Name/number of the safety notice issued | [optional] 
**subject** | **str** | Reason for the safety violation | [optional] 
**time_hour** | **int** | Time of safety violation - hour | [optional] 
**time_minute** | **int** | Time of safety violation - minute | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_safety_violation_logs_id_patch_request_safety_violation_log import RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequestSafetyViolationLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequestSafetyViolationLog from a JSON string
rest_v10_projects_project_id_safety_violation_logs_id_patch_request_safety_violation_log_instance = RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequestSafetyViolationLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequestSafetyViolationLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_safety_violation_logs_id_patch_request_safety_violation_log_dict = rest_v10_projects_project_id_safety_violation_logs_id_patch_request_safety_violation_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequestSafetyViolationLog from a dict
rest_v10_projects_project_id_safety_violation_logs_id_patch_request_safety_violation_log_from_dict = RestV10ProjectsProjectIdSafetyViolationLogsIdPatchRequestSafetyViolationLog.from_dict(rest_v10_projects_project_id_safety_violation_logs_id_patch_request_safety_violation_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


