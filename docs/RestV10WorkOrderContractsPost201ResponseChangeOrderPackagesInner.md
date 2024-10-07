# RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**due_date** | **date** | Due date | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**reviewed_at** | **datetime** | Reviewed at | [optional] 
**title** | **str** | Title | [optional] 
**status** | **str** | Status | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_change_order_packages_inner import RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner from a JSON string
rest_v10_work_order_contracts_post201_response_change_order_packages_inner_instance = RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_post201_response_change_order_packages_inner_dict = rest_v10_work_order_contracts_post201_response_change_order_packages_inner_instance.to_dict()
# create an instance of RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner from a dict
rest_v10_work_order_contracts_post201_response_change_order_packages_inner_from_dict = RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner.from_dict(rest_v10_work_order_contracts_post201_response_change_order_packages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


