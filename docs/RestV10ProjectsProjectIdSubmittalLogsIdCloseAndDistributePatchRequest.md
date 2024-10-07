# RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submittal_log_status_id** | **int** |  | [optional] 
**submittal_description** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**prostore_file_ids** | **List[int]** |  | [optional] 
**recipient_ids** | **List[int]** |  | [optional] 
**selected_approvers** | [**List[RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequestSelectedApproversInner]**](RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequestSelectedApproversInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request import RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest from a JSON string
rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request_instance = RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request_dict = rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest from a dict
rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request_from_dict = RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest.from_dict(rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


