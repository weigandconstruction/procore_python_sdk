# WorkflowActivityHistory

Workflow Activity History object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_activity_id** | **int** | Workflow Activity ID | 
**workflow_instance_id** | **int** | Workflow Instance ID | 
**workflow_user_role_id** | **int** | Workflow User Role ID | 
**performed_by_id** | **int** | Login Information ID of a Workflow User Role Login Information. | 
**comments** | **str** | Comments | [optional] 
**attachments** | **List[str]** | Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.workflow_activity_history import WorkflowActivityHistory

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowActivityHistory from a JSON string
workflow_activity_history_instance = WorkflowActivityHistory.from_json(json)
# print the JSON string representation of the object
print(WorkflowActivityHistory.to_json())

# convert the object into a dict
workflow_activity_history_dict = workflow_activity_history_instance.to_dict()
# create an instance of WorkflowActivityHistory from a dict
workflow_activity_history_from_dict = WorkflowActivityHistory.from_dict(workflow_activity_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


