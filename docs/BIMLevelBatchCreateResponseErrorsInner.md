# BIMLevelBatchCreateResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elevation** | **float** | Level elevation | 
**bim_file_id** | **int** | ID of the BIM File linked to the Level | 
**location_id** | **int** | ID of location linked to the Level | 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_level_batch_create_response_errors_inner import BIMLevelBatchCreateResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BIMLevelBatchCreateResponseErrorsInner from a JSON string
bim_level_batch_create_response_errors_inner_instance = BIMLevelBatchCreateResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(BIMLevelBatchCreateResponseErrorsInner.to_json())

# convert the object into a dict
bim_level_batch_create_response_errors_inner_dict = bim_level_batch_create_response_errors_inner_instance.to_dict()
# create an instance of BIMLevelBatchCreateResponseErrorsInner from a dict
bim_level_batch_create_response_errors_inner_from_dict = BIMLevelBatchCreateResponseErrorsInner.from_dict(bim_level_batch_create_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


