# RestV10WorkflowInstancesGet200ResponseInnerProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the associated project | [optional] 
**id** | **int** | Unique identifier for the project. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_workflow_instances_get200_response_inner_project import RestV10WorkflowInstancesGet200ResponseInnerProject

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerProject from a JSON string
rest_v10_workflow_instances_get200_response_inner_project_instance = RestV10WorkflowInstancesGet200ResponseInnerProject.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkflowInstancesGet200ResponseInnerProject.to_json())

# convert the object into a dict
rest_v10_workflow_instances_get200_response_inner_project_dict = rest_v10_workflow_instances_get200_response_inner_project_instance.to_dict()
# create an instance of RestV10WorkflowInstancesGet200ResponseInnerProject from a dict
rest_v10_workflow_instances_get200_response_inner_project_from_dict = RestV10WorkflowInstancesGet200ResponseInnerProject.from_dict(rest_v10_workflow_instances_get200_response_inner_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


