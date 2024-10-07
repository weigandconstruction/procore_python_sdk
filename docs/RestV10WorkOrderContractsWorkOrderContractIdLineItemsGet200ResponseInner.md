# RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Line Item id | [optional] 
**amount** | **str** | Line Item amount | [optional] 
**company** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany.md) |  | [optional] 
**cost_code** | [**Extended**](Extended.md) |  | [optional] 
**created_at** | **datetime** | Created at date and time | [optional] 
**description** | **str** | Line Item description | [optional] 
**extended_type** | **str** | Line Item extended type | [optional] 
**holder** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerHolder**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerHolder.md) |  | [optional] 
**line_item_type** | [**LineItemType**](LineItemType.md) |  | [optional] 
**origin_data** | **str** | Line Item third party data | [optional] 
**origin_id** | **str** | Line Item third party id | [optional] 
**position** | **int** | Line Item position | [optional] 
**project** | [**RestV10WorkOrderContractsGet200ResponseInnerProject**](RestV10WorkOrderContractsGet200ResponseInnerProject.md) |  | [optional] 
**quantity** | **float** | Line Item quantity | [optional] 
**tax_code_id** | **int** | Tax Code ID | [optional] 
**total_amount** | **float** | Line Item total amount | [optional] 
**extended_amount** | **float** | Line Item extended amount | [optional] 
**unit_cost** | **float** | Line Item unit cost | [optional] 
**uom** | **str** | Line Item units of measure | [optional] 
**wbs_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.md) |  | [optional] 
**updated_at** | **datetime** | Updated at date and time | [optional] 
**change_event_line_item** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerChangeEventLineItem**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerChangeEventLineItem.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_get200_response_inner import RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner from a JSON string
rest_v10_work_order_contracts_work_order_contract_id_line_items_get200_response_inner_instance = RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_work_order_contract_id_line_items_get200_response_inner_dict = rest_v10_work_order_contracts_work_order_contract_id_line_items_get200_response_inner_instance.to_dict()
# create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner from a dict
rest_v10_work_order_contracts_work_order_contract_id_line_items_get200_response_inner_from_dict = RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner.from_dict(rest_v10_work_order_contracts_work_order_contract_id_line_items_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


