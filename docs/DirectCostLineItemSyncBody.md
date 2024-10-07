# DirectCostLineItemSyncBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[LineItem]**](LineItem.md) |  | 

## Example

```python
from procore_sdk.models.direct_cost_line_item_sync_body import DirectCostLineItemSyncBody

# TODO update the JSON string below
json = "{}"
# create an instance of DirectCostLineItemSyncBody from a JSON string
direct_cost_line_item_sync_body_instance = DirectCostLineItemSyncBody.from_json(json)
# print the JSON string representation of the object
print(DirectCostLineItemSyncBody.to_json())

# convert the object into a dict
direct_cost_line_item_sync_body_dict = direct_cost_line_item_sync_body_instance.to_dict()
# create an instance of DirectCostLineItemSyncBody from a dict
direct_cost_line_item_sync_body_from_dict = DirectCostLineItemSyncBody.from_dict(direct_cost_line_item_sync_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


