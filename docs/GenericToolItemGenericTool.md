# GenericToolItemGenericTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Title | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_item_generic_tool import GenericToolItemGenericTool

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItemGenericTool from a JSON string
generic_tool_item_generic_tool_instance = GenericToolItemGenericTool.from_json(json)
# print the JSON string representation of the object
print(GenericToolItemGenericTool.to_json())

# convert the object into a dict
generic_tool_item_generic_tool_dict = generic_tool_item_generic_tool_instance.to_dict()
# create an instance of GenericToolItemGenericTool from a dict
generic_tool_item_generic_tool_from_dict = GenericToolItemGenericTool.from_dict(generic_tool_item_generic_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


