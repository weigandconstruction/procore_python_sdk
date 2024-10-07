# Upload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_filename** | **str** | By setting a filename you ensure that the storage service knows the filename of the upload. Files are often downloaded directly from the storage service and without the filename they will save on the end users&#39; device without a readable name or extension. | 
**response_content_type** | **str** | The content-type set through this parameter will be used by the storage service during download just like the response_filename. Setting this value is less important because HTTP clients and operating systems are generally well equipped to determine file types.  Setting this parameter is optional and should only be included when you are certain it&#39;s correct or when you want to force a content-type other than what the filename extension suggests. | [optional] 
**attachment_content_disposition** | **bool** | The content type set through this parameter will be used by the storage system during download, similar to the response_filename. When set to true, the file will be downloaded as an attachment. Otherwise, the file content will be rendered inline in the browser. | [optional] 
**segments** | [**List[UploadSegmentsInner]**](UploadSegmentsInner.md) | Upload segments | [optional] 

## Example

```python
from procore_sdk.models.upload import Upload

# TODO update the JSON string below
json = "{}"
# create an instance of Upload from a JSON string
upload_instance = Upload.from_json(json)
# print the JSON string representation of the object
print(Upload.to_json())

# convert the object into a dict
upload_dict = upload_instance.to_dict()
# create an instance of Upload from a dict
upload_from_dict = Upload.from_dict(upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


