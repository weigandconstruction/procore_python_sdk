# Default1ChangeOrderChangeReason

Change order change reason entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**change_reason** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.default1_change_order_change_reason import Default1ChangeOrderChangeReason

# TODO update the JSON string below
json = "{}"
# create an instance of Default1ChangeOrderChangeReason from a JSON string
default1_change_order_change_reason_instance = Default1ChangeOrderChangeReason.from_json(json)
# print the JSON string representation of the object
print(Default1ChangeOrderChangeReason.to_json())

# convert the object into a dict
default1_change_order_change_reason_dict = default1_change_order_change_reason_instance.to_dict()
# create an instance of Default1ChangeOrderChangeReason from a dict
default1_change_order_change_reason_from_dict = Default1ChangeOrderChangeReason.from_dict(default1_change_order_change_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


