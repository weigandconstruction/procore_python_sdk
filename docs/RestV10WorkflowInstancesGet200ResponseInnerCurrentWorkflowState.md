# RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowState

Workflow State

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**status** | **str** | Status | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_workflow_instances_get200_response_inner_current_workflow_state import RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowState

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowState from a JSON string
rest_v10_workflow_instances_get200_response_inner_current_workflow_state_instance = RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowState.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowState.to_json())

# convert the object into a dict
rest_v10_workflow_instances_get200_response_inner_current_workflow_state_dict = rest_v10_workflow_instances_get200_response_inner_current_workflow_state_instance.to_dict()
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowState from a dict
rest_v10_workflow_instances_get200_response_inner_current_workflow_state_from_dict = RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowState.from_dict(rest_v10_workflow_instances_get200_response_inner_current_workflow_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


