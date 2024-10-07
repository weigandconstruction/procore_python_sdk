# RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner


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
**updated_at** | **datetime** | Updated at | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_change_order_requests_inner_inner import RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner from a JSON string
rest_v10_work_order_contracts_post201_response_change_order_requests_inner_inner_instance = RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_post201_response_change_order_requests_inner_inner_dict = rest_v10_work_order_contracts_post201_response_change_order_requests_inner_inner_instance.to_dict()
# create an instance of RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner from a dict
rest_v10_work_order_contracts_post201_response_change_order_requests_inner_inner_from_dict = RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner.from_dict(rest_v10_work_order_contracts_post201_response_change_order_requests_inner_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


