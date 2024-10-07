# RestV10ChangeOrderRequestsPostRequestChangeOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from procore_sdk.models.rest_v10_change_order_requests_post_request_change_order import RestV10ChangeOrderRequestsPostRequestChangeOrder

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderRequestsPostRequestChangeOrder from a JSON string
rest_v10_change_order_requests_post_request_change_order_instance = RestV10ChangeOrderRequestsPostRequestChangeOrder.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderRequestsPostRequestChangeOrder.to_json())

# convert the object into a dict
rest_v10_change_order_requests_post_request_change_order_dict = rest_v10_change_order_requests_post_request_change_order_instance.to_dict()
# create an instance of RestV10ChangeOrderRequestsPostRequestChangeOrder from a dict
rest_v10_change_order_requests_post_request_change_order_from_dict = RestV10ChangeOrderRequestsPostRequestChangeOrder.from_dict(rest_v10_change_order_requests_post_request_change_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


