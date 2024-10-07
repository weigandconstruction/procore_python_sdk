# RestV10PurchaseOrderContractsSyncPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[RestV10PurchaseOrderContractsGet200ResponseInner]**](RestV10PurchaseOrderContractsGet200ResponseInner.md) |  | [optional] 
**errors** | **List[object]** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_purchase_order_contracts_sync_patch200_response import RestV10PurchaseOrderContractsSyncPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PurchaseOrderContractsSyncPatch200Response from a JSON string
rest_v10_purchase_order_contracts_sync_patch200_response_instance = RestV10PurchaseOrderContractsSyncPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10PurchaseOrderContractsSyncPatch200Response.to_json())

# convert the object into a dict
rest_v10_purchase_order_contracts_sync_patch200_response_dict = rest_v10_purchase_order_contracts_sync_patch200_response_instance.to_dict()
# create an instance of RestV10PurchaseOrderContractsSyncPatch200Response from a dict
rest_v10_purchase_order_contracts_sync_patch200_response_from_dict = RestV10PurchaseOrderContractsSyncPatch200Response.from_dict(rest_v10_purchase_order_contracts_sync_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


