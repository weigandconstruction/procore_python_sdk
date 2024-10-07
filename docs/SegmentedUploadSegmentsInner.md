# SegmentedUploadSegmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | Entity tag. Hash of S3 object. | [optional] 
**sha256** | **str** | SHA-256 hash of the file segment. | [optional] 
**size** | [**SegmentedUploadSegmentsInnerSize**](SegmentedUploadSegmentsInnerSize.md) |  | [optional] 
**url** | **str** | Segment url | [optional] 
**headers** | [**SegmentedUploadSegmentsInnerHeaders**](SegmentedUploadSegmentsInnerHeaders.md) |  | [optional] 

## Example

```python
from procore_sdk.models.segmented_upload_segments_inner import SegmentedUploadSegmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentedUploadSegmentsInner from a JSON string
segmented_upload_segments_inner_instance = SegmentedUploadSegmentsInner.from_json(json)
# print the JSON string representation of the object
print(SegmentedUploadSegmentsInner.to_json())

# convert the object into a dict
segmented_upload_segments_inner_dict = segmented_upload_segments_inner_instance.to_dict()
# create an instance of SegmentedUploadSegmentsInner from a dict
segmented_upload_segments_inner_from_dict = SegmentedUploadSegmentsInner.from_dict(segmented_upload_segments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


