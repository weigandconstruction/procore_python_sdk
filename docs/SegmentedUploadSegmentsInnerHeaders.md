# SegmentedUploadSegmentsInnerHeaders

Amazon headers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_amz_content_sha256** | **str** | Segment sha256 | [optional] 
**content_length** | **str** | Segment size | [optional] 

## Example

```python
from procore_sdk.models.segmented_upload_segments_inner_headers import SegmentedUploadSegmentsInnerHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentedUploadSegmentsInnerHeaders from a JSON string
segmented_upload_segments_inner_headers_instance = SegmentedUploadSegmentsInnerHeaders.from_json(json)
# print the JSON string representation of the object
print(SegmentedUploadSegmentsInnerHeaders.to_json())

# convert the object into a dict
segmented_upload_segments_inner_headers_dict = segmented_upload_segments_inner_headers_instance.to_dict()
# create an instance of SegmentedUploadSegmentsInnerHeaders from a dict
segmented_upload_segments_inner_headers_from_dict = SegmentedUploadSegmentsInnerHeaders.from_dict(segmented_upload_segments_inner_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


