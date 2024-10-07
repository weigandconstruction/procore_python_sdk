# SegmentedUpload

An Upload resource contains instructions on how to upload files directly to Procore's storage service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Reference to the upload that stays valid during the lifecycle of the upload. After uploading to the storage service you will use this reference to associate the upload to another resource. | [optional] 
**status** | **str** | Upload status. | [optional] 
**segments** | [**List[SegmentedUploadSegmentsInner]**](SegmentedUploadSegmentsInner.md) | Upload segments. Optional. | [optional] 

## Example

```python
from procore_sdk.models.segmented_upload import SegmentedUpload

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentedUpload from a JSON string
segmented_upload_instance = SegmentedUpload.from_json(json)
# print the JSON string representation of the object
print(SegmentedUpload.to_json())

# convert the object into a dict
segmented_upload_dict = segmented_upload_instance.to_dict()
# create an instance of SegmentedUpload from a dict
segmented_upload_from_dict = SegmentedUpload.from_dict(segmented_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


