# RestV10FoldersIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | [**RestV10FoldersIdPatchRequestFolder**](RestV10FoldersIdPatchRequestFolder.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_folders_id_patch_request import RestV10FoldersIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FoldersIdPatchRequest from a JSON string
rest_v10_folders_id_patch_request_instance = RestV10FoldersIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10FoldersIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_folders_id_patch_request_dict = rest_v10_folders_id_patch_request_instance.to_dict()
# create an instance of RestV10FoldersIdPatchRequest from a dict
rest_v10_folders_id_patch_request_from_dict = RestV10FoldersIdPatchRequest.from_dict(rest_v10_folders_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


