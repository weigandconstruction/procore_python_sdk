# TheGenericToolObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the generic tool. | 
**abbreviation** | **str** | An abbreviation for the generic tool. | [optional] 
**private_by_default** | **bool** | If this property is set to true, any items that are created for the tool are private by default. | [optional] 
**new_project_default** | **bool** | If this property is set to true, the generic tool will be added to new projects by default. | [optional] 
**send_overdue_notifications** | **bool** | If this property is set to true, notifications will be sent to assignees when an item is overdue. | [optional] 

## Example

```python
from procore_sdk.models.the_generic_tool_object import TheGenericToolObject

# TODO update the JSON string below
json = "{}"
# create an instance of TheGenericToolObject from a JSON string
the_generic_tool_object_instance = TheGenericToolObject.from_json(json)
# print the JSON string representation of the object
print(TheGenericToolObject.to_json())

# convert the object into a dict
the_generic_tool_object_dict = the_generic_tool_object_instance.to_dict()
# create an instance of TheGenericToolObject from a dict
the_generic_tool_object_from_dict = TheGenericToolObject.from_dict(the_generic_tool_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


