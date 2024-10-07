# BIMFileUploadMetadataLinkedFilesInner

Linked file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of linked file | [optional] 
**saved_path** | **str** | Path of linked file | [optional] 
**path_type** | **str** | Type of path | [optional] 

## Example

```python
from procore_sdk.models.bim_file_upload_metadata_linked_files_inner import BIMFileUploadMetadataLinkedFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileUploadMetadataLinkedFilesInner from a JSON string
bim_file_upload_metadata_linked_files_inner_instance = BIMFileUploadMetadataLinkedFilesInner.from_json(json)
# print the JSON string representation of the object
print(BIMFileUploadMetadataLinkedFilesInner.to_json())

# convert the object into a dict
bim_file_upload_metadata_linked_files_inner_dict = bim_file_upload_metadata_linked_files_inner_instance.to_dict()
# create an instance of BIMFileUploadMetadataLinkedFilesInner from a dict
bim_file_upload_metadata_linked_files_inner_from_dict = BIMFileUploadMetadataLinkedFilesInner.from_dict(bim_file_upload_metadata_linked_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


