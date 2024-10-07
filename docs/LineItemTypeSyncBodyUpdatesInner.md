# LineItemTypeSyncBodyUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Line Item Type ID | [optional] 
**name** | **str** | Line Item Type name | [optional] 
**csv_import_code** | **str** | Abbreviation code | [optional] 
**base_type** | **str** | Base type | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.line_item_type_sync_body_updates_inner import LineItemTypeSyncBodyUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemTypeSyncBodyUpdatesInner from a JSON string
line_item_type_sync_body_updates_inner_instance = LineItemTypeSyncBodyUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(LineItemTypeSyncBodyUpdatesInner.to_json())

# convert the object into a dict
line_item_type_sync_body_updates_inner_dict = line_item_type_sync_body_updates_inner_instance.to_dict()
# create an instance of LineItemTypeSyncBodyUpdatesInner from a dict
line_item_type_sync_body_updates_inner_from_dict = LineItemTypeSyncBodyUpdatesInner.from_dict(line_item_type_sync_body_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


