# Commitment1ChangeOrderRequestsInnerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**due_date** | **date** | Due date | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**change_order_package_id** | **int** | Change Order Package ID | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.commitment1_change_order_requests_inner_inner import Commitment1ChangeOrderRequestsInnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of Commitment1ChangeOrderRequestsInnerInner from a JSON string
commitment1_change_order_requests_inner_inner_instance = Commitment1ChangeOrderRequestsInnerInner.from_json(json)
# print the JSON string representation of the object
print(Commitment1ChangeOrderRequestsInnerInner.to_json())

# convert the object into a dict
commitment1_change_order_requests_inner_inner_dict = commitment1_change_order_requests_inner_inner_instance.to_dict()
# create an instance of Commitment1ChangeOrderRequestsInnerInner from a dict
commitment1_change_order_requests_inner_inner_from_dict = Commitment1ChangeOrderRequestsInnerInner.from_dict(commitment1_change_order_requests_inner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


