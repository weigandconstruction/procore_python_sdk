# ChangeOrderRequestSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[ChangeOrderRequestSyncUpdatesInner]**](ChangeOrderRequestSyncUpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.change_order_request_sync import ChangeOrderRequestSync

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOrderRequestSync from a JSON string
change_order_request_sync_instance = ChangeOrderRequestSync.from_json(json)
# print the JSON string representation of the object
print(ChangeOrderRequestSync.to_json())

# convert the object into a dict
change_order_request_sync_dict = change_order_request_sync_instance.to_dict()
# create an instance of ChangeOrderRequestSync from a dict
change_order_request_sync_from_dict = ChangeOrderRequestSync.from_dict(change_order_request_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


