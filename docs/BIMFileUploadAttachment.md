# BIMFileUploadAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**size** | **float** |  | [optional] 

## Example

```python
from procore_sdk.models.bim_file_upload_attachment import BIMFileUploadAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileUploadAttachment from a JSON string
bim_file_upload_attachment_instance = BIMFileUploadAttachment.from_json(json)
# print the JSON string representation of the object
print(BIMFileUploadAttachment.to_json())

# convert the object into a dict
bim_file_upload_attachment_dict = bim_file_upload_attachment_instance.to_dict()
# create an instance of BIMFileUploadAttachment from a dict
bim_file_upload_attachment_from_dict = BIMFileUploadAttachment.from_dict(bim_file_upload_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


