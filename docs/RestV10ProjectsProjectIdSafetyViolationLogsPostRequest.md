# RestV10ProjectsProjectIdSafetyViolationLogsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**safety_violation_log** | [**RestV10ProjectsProjectIdSafetyViolationLogsPostRequestSafetyViolationLog**](RestV10ProjectsProjectIdSafetyViolationLogsPostRequestSafetyViolationLog.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_safety_violation_logs_post_request import RestV10ProjectsProjectIdSafetyViolationLogsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSafetyViolationLogsPostRequest from a JSON string
rest_v10_projects_project_id_safety_violation_logs_post_request_instance = RestV10ProjectsProjectIdSafetyViolationLogsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSafetyViolationLogsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_safety_violation_logs_post_request_dict = rest_v10_projects_project_id_safety_violation_logs_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSafetyViolationLogsPostRequest from a dict
rest_v10_projects_project_id_safety_violation_logs_post_request_from_dict = RestV10ProjectsProjectIdSafetyViolationLogsPostRequest.from_dict(rest_v10_projects_project_id_safety_violation_logs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


