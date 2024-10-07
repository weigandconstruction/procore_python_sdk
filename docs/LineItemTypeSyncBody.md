# LineItemTypeSyncBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**updates** | [**List[LineItemTypeSyncBodyUpdatesInner]**](LineItemTypeSyncBodyUpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.line_item_type_sync_body import LineItemTypeSyncBody

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemTypeSyncBody from a JSON string
line_item_type_sync_body_instance = LineItemTypeSyncBody.from_json(json)
# print the JSON string representation of the object
print(LineItemTypeSyncBody.to_json())

# convert the object into a dict
line_item_type_sync_body_dict = line_item_type_sync_body_instance.to_dict()
# create an instance of LineItemTypeSyncBody from a dict
line_item_type_sync_body_from_dict = LineItemTypeSyncBody.from_dict(line_item_type_sync_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


