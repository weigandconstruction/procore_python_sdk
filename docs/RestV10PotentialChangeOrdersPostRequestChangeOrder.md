# RestV10PotentialChangeOrdersPostRequestChangeOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment_change_event_id** | **int** | Commitment Change Event ID | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **datetime** | Due date | [optional] 
**grand_total** | **float** | Total including markup | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**prime_change_event_id** | **int** | Prime Contract Change Event ID | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_potential_change_orders_post_request_change_order import RestV10PotentialChangeOrdersPostRequestChangeOrder

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PotentialChangeOrdersPostRequestChangeOrder from a JSON string
rest_v10_potential_change_orders_post_request_change_order_instance = RestV10PotentialChangeOrdersPostRequestChangeOrder.from_json(json)
# print the JSON string representation of the object
print(RestV10PotentialChangeOrdersPostRequestChangeOrder.to_json())

# convert the object into a dict
rest_v10_potential_change_orders_post_request_change_order_dict = rest_v10_potential_change_orders_post_request_change_order_instance.to_dict()
# create an instance of RestV10PotentialChangeOrdersPostRequestChangeOrder from a dict
rest_v10_potential_change_orders_post_request_change_order_from_dict = RestV10PotentialChangeOrdersPostRequestChangeOrder.from_dict(rest_v10_potential_change_orders_post_request_change_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


