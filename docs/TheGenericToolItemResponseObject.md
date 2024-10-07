# TheGenericToolItemResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**official** | **bool** | If this property is set ot true, the response is an official response. If this property is set to false, the response is not an official response. | [optional] 

## Example

```python
from procore_sdk.models.the_generic_tool_item_response_object import TheGenericToolItemResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheGenericToolItemResponseObject from a JSON string
the_generic_tool_item_response_object_instance = TheGenericToolItemResponseObject.from_json(json)
# print the JSON string representation of the object
print(TheGenericToolItemResponseObject.to_json())

# convert the object into a dict
the_generic_tool_item_response_object_dict = the_generic_tool_item_response_object_instance.to_dict()
# create an instance of TheGenericToolItemResponseObject from a dict
the_generic_tool_item_response_object_from_dict = TheGenericToolItemResponseObject.from_dict(the_generic_tool_item_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


