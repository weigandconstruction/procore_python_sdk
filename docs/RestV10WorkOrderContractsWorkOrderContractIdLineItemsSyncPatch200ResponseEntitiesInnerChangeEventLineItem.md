# RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem

Change Event Line Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Change Event Line Item ID | [optional] 
**cost_rom** | **float** | Change Event Line Item Cost ROM | [optional] 
**revenue_rom** | **float** | Change Event Line Item Revenue ROM | [optional] 
**event_id** | **int** | Change Event ID | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**line_item_type** | [**LineItemType**](LineItemType.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_entities_inner_change_event_line_item import RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem from a JSON string
rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_entities_inner_change_event_line_item_instance = RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_entities_inner_change_event_line_item_dict = rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_entities_inner_change_event_line_item_instance.to_dict()
# create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem from a dict
rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_entities_inner_change_event_line_item_from_dict = RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem.from_dict(rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_entities_inner_change_event_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


