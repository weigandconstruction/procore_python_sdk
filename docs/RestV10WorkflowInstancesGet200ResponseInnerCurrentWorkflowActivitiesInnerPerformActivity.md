# RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivity

Endpoint to perform Workflow Activities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to perform the Workflow Activity | [optional] 
**method** | **str** | HTTP Method with which to request the URL | [optional] 
**data** | [**RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivityData**](RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivityData.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_perform_activity import RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivity

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivity from a JSON string
rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_perform_activity_instance = RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivity.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivity.to_json())

# convert the object into a dict
rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_perform_activity_dict = rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_perform_activity_instance.to_dict()
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivity from a dict
rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_perform_activity_from_dict = RestV10WorkflowInstancesGet200ResponseInnerCurrentWorkflowActivitiesInnerPerformActivity.from_dict(rest_v10_workflow_instances_get200_response_inner_current_workflow_activities_inner_perform_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


