# RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRole

Workflow User Role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**assignee** | [**RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRoleAssignee**](RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRoleAssignee.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_workflow_user_role import RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRole

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRole from a JSON string
rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_workflow_user_role_instance = RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRole.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRole.to_json())

# convert the object into a dict
rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_workflow_user_role_dict = rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_workflow_user_role_instance.to_dict()
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRole from a dict
rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_workflow_user_role_from_dict = RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerWorkflowUserRole.from_dict(rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_workflow_user_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


