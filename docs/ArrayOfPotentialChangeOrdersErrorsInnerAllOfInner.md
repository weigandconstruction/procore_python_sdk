# ArrayOfPotentialChangeOrdersErrorsInnerAllOfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**due_date** | **date** | Due date | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**reviewed_at** | **datetime** | Reviewed at | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.array_of_potential_change_orders_errors_inner_all_of_inner import ArrayOfPotentialChangeOrdersErrorsInnerAllOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPotentialChangeOrdersErrorsInnerAllOfInner from a JSON string
array_of_potential_change_orders_errors_inner_all_of_inner_instance = ArrayOfPotentialChangeOrdersErrorsInnerAllOfInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfPotentialChangeOrdersErrorsInnerAllOfInner.to_json())

# convert the object into a dict
array_of_potential_change_orders_errors_inner_all_of_inner_dict = array_of_potential_change_orders_errors_inner_all_of_inner_instance.to_dict()
# create an instance of ArrayOfPotentialChangeOrdersErrorsInnerAllOfInner from a dict
array_of_potential_change_orders_errors_inner_all_of_inner_from_dict = ArrayOfPotentialChangeOrdersErrorsInnerAllOfInner.from_dict(array_of_potential_change_orders_errors_inner_all_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


