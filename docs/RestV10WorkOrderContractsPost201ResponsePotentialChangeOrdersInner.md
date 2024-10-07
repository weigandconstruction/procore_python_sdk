# RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner


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
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_potential_change_orders_inner import RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner from a JSON string
rest_v10_work_order_contracts_post201_response_potential_change_orders_inner_instance = RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_post201_response_potential_change_orders_inner_dict = rest_v10_work_order_contracts_post201_response_potential_change_orders_inner_instance.to_dict()
# create an instance of RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner from a dict
rest_v10_work_order_contracts_post201_response_potential_change_orders_inner_from_dict = RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner.from_dict(rest_v10_work_order_contracts_post201_response_potential_change_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


