# BIMFileUpload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_file_id** | **int** | ID of the associated BIM File | [optional] 
**document_upload_id** | **int** | ID of the associated Document Upload | [optional] 
**file_version** | [**BIMFileUploadFileVersion**](BIMFileUploadFileVersion.md) |  | [optional] 
**attachment** | [**BIMFileUploadAttachment**](BIMFileUploadAttachment.md) |  | [optional] 
**created_by** | [**BIMFileUploadCreatedBy**](BIMFileUploadCreatedBy.md) |  | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**metadata** | [**BIMFileUploadMetadata**](BIMFileUploadMetadata.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_file_upload import BIMFileUpload

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileUpload from a JSON string
bim_file_upload_instance = BIMFileUpload.from_json(json)
# print the JSON string representation of the object
print(BIMFileUpload.to_json())

# convert the object into a dict
bim_file_upload_dict = bim_file_upload_instance.to_dict()
# create an instance of BIMFileUpload from a dict
bim_file_upload_from_dict = BIMFileUpload.from_dict(bim_file_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


