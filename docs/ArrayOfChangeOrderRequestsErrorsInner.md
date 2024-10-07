# ArrayOfChangeOrderRequestsErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**change_order_package_id** | **int** | Change Order Package ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**creator** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **datetime** | Due date | [optional] 
**grand_total** | **float** | Total including markup | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**position** | **int** | Position | [optional] 
**private** | **bool** | If true, visible to admins only; otherwise visible to those with access to the parent contract. | [optional] 
**revision** | **int** | Revision | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_change_order_requests_errors_inner import ArrayOfChangeOrderRequestsErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfChangeOrderRequestsErrorsInner from a JSON string
array_of_change_order_requests_errors_inner_instance = ArrayOfChangeOrderRequestsErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfChangeOrderRequestsErrorsInner.to_json())

# convert the object into a dict
array_of_change_order_requests_errors_inner_dict = array_of_change_order_requests_errors_inner_instance.to_dict()
# create an instance of ArrayOfChangeOrderRequestsErrorsInner from a dict
array_of_change_order_requests_errors_inner_from_dict = ArrayOfChangeOrderRequestsErrorsInner.from_dict(array_of_change_order_requests_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


