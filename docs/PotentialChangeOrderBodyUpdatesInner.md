# PotentialChangeOrderBodyUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_order_request_id** | **int** | Change Order Request ID | [optional] 
**change_order_request** | [**PotentialChangeOrderBodyUpdatesInnerChangeOrderRequest**](PotentialChangeOrderBodyUpdatesInnerChangeOrderRequest.md) |  | [optional] 
**commitment_change_event_id** | **int** | Commitment Change Event ID | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **datetime** | Due date | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**prime_change_event_id** | **int** | Prime Contract Change Event ID | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**status** | **str** | Status. This PCO attribute is ignored on projects when the tool is configured for single tier COs. | [optional] 
**title** | **str** | Title | [optional] 

## Example

```python
from procore_sdk.models.potential_change_order_body_updates_inner import PotentialChangeOrderBodyUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PotentialChangeOrderBodyUpdatesInner from a JSON string
potential_change_order_body_updates_inner_instance = PotentialChangeOrderBodyUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(PotentialChangeOrderBodyUpdatesInner.to_json())

# convert the object into a dict
potential_change_order_body_updates_inner_dict = potential_change_order_body_updates_inner_instance.to_dict()
# create an instance of PotentialChangeOrderBodyUpdatesInner from a dict
potential_change_order_body_updates_inner_from_dict = PotentialChangeOrderBodyUpdatesInner.from_dict(potential_change_order_body_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


