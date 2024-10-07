# RestV10ChangeOrderPackagesPostRequestChangeOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**description** | **str** | Description | [optional] 
**grand_total** | **str** | Total including markup | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**due_date** | **date** | Due date | [optional] 
**executed** | **bool** | Executed | [optional] 
**signed_change_order_received_date** | **date** | Signed change order received date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_order_packages_post_request_change_order import RestV10ChangeOrderPackagesPostRequestChangeOrder

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderPackagesPostRequestChangeOrder from a JSON string
rest_v10_change_order_packages_post_request_change_order_instance = RestV10ChangeOrderPackagesPostRequestChangeOrder.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderPackagesPostRequestChangeOrder.to_json())

# convert the object into a dict
rest_v10_change_order_packages_post_request_change_order_dict = rest_v10_change_order_packages_post_request_change_order_instance.to_dict()
# create an instance of RestV10ChangeOrderPackagesPostRequestChangeOrder from a dict
rest_v10_change_order_packages_post_request_change_order_from_dict = RestV10ChangeOrderPackagesPostRequestChangeOrder.from_dict(rest_v10_change_order_packages_post_request_change_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


