# RestV10WorkflowInstancesGet200ResponseInnerWorkflow

Workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**class_name** | **str** | Class Name | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Created at | [optional] 
**domain** | **str** | Domain name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_workflow_instances_get200_response_inner_workflow import RestV10WorkflowInstancesGet200ResponseInnerWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerWorkflow from a JSON string
rest_v10_workflow_instances_get200_response_inner_workflow_instance = RestV10WorkflowInstancesGet200ResponseInnerWorkflow.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkflowInstancesGet200ResponseInnerWorkflow.to_json())

# convert the object into a dict
rest_v10_workflow_instances_get200_response_inner_workflow_dict = rest_v10_workflow_instances_get200_response_inner_workflow_instance.to_dict()
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerWorkflow from a dict
rest_v10_workflow_instances_get200_response_inner_workflow_from_dict = RestV10WorkflowInstancesGet200ResponseInnerWorkflow.from_dict(rest_v10_workflow_instances_get200_response_inner_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


