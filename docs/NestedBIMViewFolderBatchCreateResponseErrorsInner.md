# NestedBIMViewFolderBatchCreateResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[str]** |  | 
**bim_file_id** | **int** | Id of BimFile to associate | 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.nested_bim_view_folder_batch_create_response_errors_inner import NestedBIMViewFolderBatchCreateResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NestedBIMViewFolderBatchCreateResponseErrorsInner from a JSON string
nested_bim_view_folder_batch_create_response_errors_inner_instance = NestedBIMViewFolderBatchCreateResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(NestedBIMViewFolderBatchCreateResponseErrorsInner.to_json())

# convert the object into a dict
nested_bim_view_folder_batch_create_response_errors_inner_dict = nested_bim_view_folder_batch_create_response_errors_inner_instance.to_dict()
# create an instance of NestedBIMViewFolderBatchCreateResponseErrorsInner from a dict
nested_bim_view_folder_batch_create_response_errors_inner_from_dict = NestedBIMViewFolderBatchCreateResponseErrorsInner.from_dict(nested_bim_view_folder_batch_create_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


