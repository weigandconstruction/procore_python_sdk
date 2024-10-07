# GenericToolItemTradesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Trade ID | [optional] 
**name** | **str** | Trade name | [optional] 
**active** | **bool** | Trade availability | [optional] 
**updated_at** | **datetime** | Timestamp of last update to Trade | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_item_trades_inner import GenericToolItemTradesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItemTradesInner from a JSON string
generic_tool_item_trades_inner_instance = GenericToolItemTradesInner.from_json(json)
# print the JSON string representation of the object
print(GenericToolItemTradesInner.to_json())

# convert the object into a dict
generic_tool_item_trades_inner_dict = generic_tool_item_trades_inner_instance.to_dict()
# create an instance of GenericToolItemTradesInner from a dict
generic_tool_item_trades_inner_from_dict = GenericToolItemTradesInner.from_dict(generic_tool_item_trades_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


