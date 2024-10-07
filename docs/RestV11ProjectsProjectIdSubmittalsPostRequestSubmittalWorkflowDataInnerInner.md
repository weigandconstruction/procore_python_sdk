# RestV11ProjectsProjectIdSubmittalsPostRequestSubmittalWorkflowDataInnerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_information_id** | **int** | The id of the user in the workflow | [optional] 
**approver_type** | **str** | The role of the user in the workflow | [optional] 
**days_to_respond** | **int** | The amount of days to respond to workflow item. *Please use either days_to_respond or due_date (days_to_respond takes precedence over due_date) | [optional] 
**due_date** | **date** | The due date for the user&#39;s response. | [optional] 
**response_required** | **bool** | Designate whether or not the approver is required to respond | [optional] 
**submittal_log_approver_id** | **int** | The id of the submittal log approver in the workflow | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_post_request_submittal_workflow_data_inner_inner import RestV11ProjectsProjectIdSubmittalsPostRequestSubmittalWorkflowDataInnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsPostRequestSubmittalWorkflowDataInnerInner from a JSON string
rest_v11_projects_project_id_submittals_post_request_submittal_workflow_data_inner_inner_instance = RestV11ProjectsProjectIdSubmittalsPostRequestSubmittalWorkflowDataInnerInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsPostRequestSubmittalWorkflowDataInnerInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_post_request_submittal_workflow_data_inner_inner_dict = rest_v11_projects_project_id_submittals_post_request_submittal_workflow_data_inner_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsPostRequestSubmittalWorkflowDataInnerInner from a dict
rest_v11_projects_project_id_submittals_post_request_submittal_workflow_data_inner_inner_from_dict = RestV11ProjectsProjectIdSubmittalsPostRequestSubmittalWorkflowDataInnerInner.from_dict(rest_v11_projects_project_id_submittals_post_request_submittal_workflow_data_inner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


