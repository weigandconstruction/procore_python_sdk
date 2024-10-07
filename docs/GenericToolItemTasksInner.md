# GenericToolItemTasksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task ID | [optional] 
**name** | **str** | Full Task name | [optional] 
**task_name** | **str** | Task name | [optional] 
**key** | **str** | Task Key | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_item_tasks_inner import GenericToolItemTasksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItemTasksInner from a JSON string
generic_tool_item_tasks_inner_instance = GenericToolItemTasksInner.from_json(json)
# print the JSON string representation of the object
print(GenericToolItemTasksInner.to_json())

# convert the object into a dict
generic_tool_item_tasks_inner_dict = generic_tool_item_tasks_inner_instance.to_dict()
# create an instance of GenericToolItemTasksInner from a dict
generic_tool_item_tasks_inner_from_dict = GenericToolItemTasksInner.from_dict(generic_tool_item_tasks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


