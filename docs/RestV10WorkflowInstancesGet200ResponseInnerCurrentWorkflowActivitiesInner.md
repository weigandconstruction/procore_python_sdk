# RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInner

Workflow Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**workflow_user_role** | [**RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRole**](RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRole.md) |  | [optional] 
**perform_activity** | [**RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivity**](RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivity.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner import RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInner from a JSON string
rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_instance = RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInner.to_json())

# convert the object into a dict
rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_dict = rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_instance.to_dict()
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInner from a dict
rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_from_dict = RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInner.from_dict(rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


