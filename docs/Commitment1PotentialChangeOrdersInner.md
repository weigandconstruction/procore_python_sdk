# Commitment1PotentialChangeOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Potential change order id | [optional] 
**created_at** | **datetime** | Potential change order created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**due_date** | **date** | Potential change order due date | [optional] 
**invoiced_date** | **date** | Potential change order invoiced date | [optional] 
**number** | **str** | Potential change order number | [optional] 
**paid_date** | **date** | Potential change order paid date | [optional] 
**reviewed_at** | **datetime** | Potential change order reviewed at | [optional] 
**title** | **str** | Potential change order title | [optional] 
**status** | **str** | Potential change order status | [optional] 
**updated_at** | **datetime** | Potential change order updated at | [optional] 

## Example

```python
from procore_sdk.models.commitment1_potential_change_orders_inner import Commitment1PotentialChangeOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of Commitment1PotentialChangeOrdersInner from a JSON string
commitment1_potential_change_orders_inner_instance = Commitment1PotentialChangeOrdersInner.from_json(json)
# print the JSON string representation of the object
print(Commitment1PotentialChangeOrdersInner.to_json())

# convert the object into a dict
commitment1_potential_change_orders_inner_dict = commitment1_potential_change_orders_inner_instance.to_dict()
# create an instance of Commitment1PotentialChangeOrdersInner from a dict
commitment1_potential_change_orders_inner_from_dict = Commitment1PotentialChangeOrdersInner.from_dict(commitment1_potential_change_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


