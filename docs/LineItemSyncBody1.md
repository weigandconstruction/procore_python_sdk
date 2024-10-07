# LineItemSyncBody1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[LineItem1]**](LineItem1.md) |  | 

## Example

```python
from procore_sdk.models.line_item_sync_body1 import LineItemSyncBody1

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemSyncBody1 from a JSON string
line_item_sync_body1_instance = LineItemSyncBody1.from_json(json)
# print the JSON string representation of the object
print(LineItemSyncBody1.to_json())

# convert the object into a dict
line_item_sync_body1_dict = line_item_sync_body1_instance.to_dict()
# create an instance of LineItemSyncBody1 from a dict
line_item_sync_body1_from_dict = LineItemSyncBody1.from_dict(line_item_sync_body1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


