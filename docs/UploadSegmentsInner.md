# UploadSegmentsInner

Upload segment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Segment file size in bytes | 
**sha256** | **str** | SHA-256 hash of the file segment | 
**md5** | **str** | MD5 checksum of the file segment | [optional] 
**etag** | **str** | Entity tag. Hash of S3 object | [optional] 

## Example

```python
from procore_sdk.models.upload_segments_inner import UploadSegmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSegmentsInner from a JSON string
upload_segments_inner_instance = UploadSegmentsInner.from_json(json)
# print the JSON string representation of the object
print(UploadSegmentsInner.to_json())

# convert the object into a dict
upload_segments_inner_dict = upload_segments_inner_instance.to_dict()
# create an instance of UploadSegmentsInner from a dict
upload_segments_inner_from_dict = UploadSegmentsInner.from_dict(upload_segments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


