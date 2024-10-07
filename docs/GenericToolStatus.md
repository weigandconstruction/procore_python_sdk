# GenericToolStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_name** | **str** | The name of the generic tool status. | 
**status** | **str** | The status of the generic tool status. | 

## Example

```python
from procore_sdk.models.generic_tool_status import GenericToolStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolStatus from a JSON string
generic_tool_status_instance = GenericToolStatus.from_json(json)
# print the JSON string representation of the object
print(GenericToolStatus.to_json())

# convert the object into a dict
generic_tool_status_dict = generic_tool_status_instance.to_dict()
# create an instance of GenericToolStatus from a dict
generic_tool_status_from_dict = GenericToolStatus.from_dict(generic_tool_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


