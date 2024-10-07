# BIMFileUploadMetadata

Meta data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_files** | [**List[BIMFileUploadMetadataLinkedFilesInner]**](BIMFileUploadMetadataLinkedFilesInner.md) | Array of linked files | [optional] 
**drawing_sheets** | [**List[BIMFileUploadMetadataDrawingSheetsInner]**](BIMFileUploadMetadataDrawingSheetsInner.md) | Array of drawing sheets | [optional] 
**file_type** | **str** | File Type (either 2d or 3d) | [optional] 

## Example

```python
from procore_sdk.models.bim_file_upload_metadata import BIMFileUploadMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileUploadMetadata from a JSON string
bim_file_upload_metadata_instance = BIMFileUploadMetadata.from_json(json)
# print the JSON string representation of the object
print(BIMFileUploadMetadata.to_json())

# convert the object into a dict
bim_file_upload_metadata_dict = bim_file_upload_metadata_instance.to_dict()
# create an instance of BIMFileUploadMetadata from a dict
bim_file_upload_metadata_from_dict = BIMFileUploadMetadata.from_dict(bim_file_upload_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


