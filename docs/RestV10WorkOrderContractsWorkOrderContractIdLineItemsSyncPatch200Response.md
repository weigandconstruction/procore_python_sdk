# RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response

Line Item Sync

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInner]**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInner.md) |  | [optional] 
**errors** | [**List[RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInner]**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response import RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response from a JSON string
rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_instance = RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_dict = rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_instance.to_dict()
# create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response from a dict
rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_from_dict = RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response.from_dict(rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


