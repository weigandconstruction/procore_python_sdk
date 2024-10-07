# RestV10TaxTypesSyncPatch200ResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Tax Type | [optional] 
**description** | **str** | Description of the Tax Type | [optional] 
**name** | **str** | The Name of the Tax Type | [optional] 
**origin_data** | **str** | Additional Third-party Metadata for the Tax Type. Note: This is a free-form text field. | [optional] 
**origin_id** | **str** | The Third-party ID of the Tax Type | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_tax_types_sync_patch200_response_errors_inner import RestV10TaxTypesSyncPatch200ResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaxTypesSyncPatch200ResponseErrorsInner from a JSON string
rest_v10_tax_types_sync_patch200_response_errors_inner_instance = RestV10TaxTypesSyncPatch200ResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10TaxTypesSyncPatch200ResponseErrorsInner.to_json())

# convert the object into a dict
rest_v10_tax_types_sync_patch200_response_errors_inner_dict = rest_v10_tax_types_sync_patch200_response_errors_inner_instance.to_dict()
# create an instance of RestV10TaxTypesSyncPatch200ResponseErrorsInner from a dict
rest_v10_tax_types_sync_patch200_response_errors_inner_from_dict = RestV10TaxTypesSyncPatch200ResponseErrorsInner.from_dict(rest_v10_tax_types_sync_patch200_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


