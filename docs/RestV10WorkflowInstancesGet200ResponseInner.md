# RestV10WorkflowInstancesGet200ResponseInner

Workflow Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**becomes_overdue_at** | **datetime** | Workflowed Object is considered overdue after | [optional] 
**current_state_set_at** | **datetime** | Workflow entered the current state at | [optional] 
**workflowed_object_id** | **int** | Workflowed Object ID | [optional] 
**workflowed_object_type** | **str** | The Type of the Workflowed Object | [optional] 
**project** | [**RestV10WorkflowInstancesGet200ResponseInnerProject**](RestV10WorkflowInstancesGet200ResponseInnerProject.md) |  | [optional] 
**current_workflow_activities** | [**List[RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInner]**](RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInner.md) |  | [optional] 
**current_workflow_state** | [**RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowState**](RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowState.md) |  | [optional] 
**workflow** | [**RestV10WorkflowInstancesGet200ResponseInnerWorkflow**](RestV10WorkflowInstancesGet200ResponseInnerWorkflow.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_workflow_instances_get200_response_inner import RestV10WorkflowInstancesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkflowInstancesGet200ResponseInner from a JSON string
rest_v10_workflow_instances_get200_response_inner_instance = RestV10WorkflowInstancesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkflowInstancesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_workflow_instances_get200_response_inner_dict = rest_v10_workflow_instances_get200_response_inner_instance.to_dict()
# create an instance of RestV10WorkflowInstancesGet200ResponseInner from a dict
rest_v10_workflow_instances_get200_response_inner_from_dict = RestV10WorkflowInstancesGet200ResponseInner.from_dict(rest_v10_workflow_instances_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


