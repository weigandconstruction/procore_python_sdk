# LineItemSyncBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[LineItem]**](LineItem.md) |  | 

## Example

```python
from procore_sdk.models.line_item_sync_body import LineItemSyncBody

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemSyncBody from a JSON string
line_item_sync_body_instance = LineItemSyncBody.from_json(json)
# print the JSON string representation of the object
print(LineItemSyncBody.to_json())

# convert the object into a dict
line_item_sync_body_dict = line_item_sync_body_instance.to_dict()
# create an instance of LineItemSyncBody from a dict
line_item_sync_body_from_dict = LineItemSyncBody.from_dict(line_item_sync_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


