# NestedBIMViewFolderBatchCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_view_folders** | [**List[RestV10NestedBimViewFoldersPost200Response]**](RestV10NestedBimViewFoldersPost200Response.md) |  | [optional] 
**errors** | [**List[NestedBIMViewFolderBatchCreateResponseErrorsInner]**](NestedBIMViewFolderBatchCreateResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.nested_bim_view_folder_batch_create_response import NestedBIMViewFolderBatchCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NestedBIMViewFolderBatchCreateResponse from a JSON string
nested_bim_view_folder_batch_create_response_instance = NestedBIMViewFolderBatchCreateResponse.from_json(json)
# print the JSON string representation of the object
print(NestedBIMViewFolderBatchCreateResponse.to_json())

# convert the object into a dict
nested_bim_view_folder_batch_create_response_dict = nested_bim_view_folder_batch_create_response_instance.to_dict()
# create an instance of NestedBIMViewFolderBatchCreateResponse from a dict
nested_bim_view_folder_batch_create_response_from_dict = NestedBIMViewFolderBatchCreateResponse.from_dict(nested_bim_view_folder_batch_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


