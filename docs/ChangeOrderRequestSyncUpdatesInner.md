# ChangeOrderRequestSyncUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**change_order_package_id** | **int** | Change Order Package ID | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **datetime** | Due date | [optional] 
**grand_total** | **float** | Total including markup | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 

## Example

```python
from procore_sdk.models.change_order_request_sync_updates_inner import ChangeOrderRequestSyncUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOrderRequestSyncUpdatesInner from a JSON string
change_order_request_sync_updates_inner_instance = ChangeOrderRequestSyncUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(ChangeOrderRequestSyncUpdatesInner.to_json())

# convert the object into a dict
change_order_request_sync_updates_inner_dict = change_order_request_sync_updates_inner_instance.to_dict()
# create an instance of ChangeOrderRequestSyncUpdatesInner from a dict
change_order_request_sync_updates_inner_from_dict = ChangeOrderRequestSyncUpdatesInner.from_dict(change_order_request_sync_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


