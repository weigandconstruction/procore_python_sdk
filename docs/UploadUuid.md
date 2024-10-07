# UploadUuid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the file when downloaded | [optional] 
**notes** | **str** | Notes about the File Version | [optional] 
**upload_uuid** | **str** | UUID referencing a previously completed Upload. See Company Uploads or Project Uploads for instructions on how use uploads. You should not use both data and upload_uuid fields in the same request. | 

## Example

```python
from procore_sdk.models.upload_uuid import UploadUuid

# TODO update the JSON string below
json = "{}"
# create an instance of UploadUuid from a JSON string
upload_uuid_instance = UploadUuid.from_json(json)
# print the JSON string representation of the object
print(UploadUuid.to_json())

# convert the object into a dict
upload_uuid_dict = upload_uuid_instance.to_dict()
# create an instance of UploadUuid from a dict
upload_uuid_from_dict = UploadUuid.from_dict(upload_uuid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


