# RestV10ChangeOrderStatusesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**mapped_to_status** | **str** | Mapped to status | [optional] 
**show_in_select** | **bool** | Whether available for GUI selection | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_order_statuses_get200_response_inner import RestV10ChangeOrderStatusesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderStatusesGet200ResponseInner from a JSON string
rest_v10_change_order_statuses_get200_response_inner_instance = RestV10ChangeOrderStatusesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderStatusesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_change_order_statuses_get200_response_inner_dict = rest_v10_change_order_statuses_get200_response_inner_instance.to_dict()
# create an instance of RestV10ChangeOrderStatusesGet200ResponseInner from a dict
rest_v10_change_order_statuses_get200_response_inner_from_dict = RestV10ChangeOrderStatusesGet200ResponseInner.from_dict(rest_v10_change_order_statuses_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


