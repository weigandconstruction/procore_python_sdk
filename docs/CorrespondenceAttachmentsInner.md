# CorrespondenceAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File ID | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 
**filename** | **str** | Base name of the file without its path | [optional] 
**content_type** | **str** | A mime type or a file extension | [optional] 
**share_url** | **str** | Shareable URL(enabled on company level) or file URL | [optional] 
**viewable_type** | **str** | Document type | [optional] 
**viewable_url** | **str** | Viewable document URL | [optional] 

## Example

```python
from procore_sdk.models.correspondence_attachments_inner import CorrespondenceAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CorrespondenceAttachmentsInner from a JSON string
correspondence_attachments_inner_instance = CorrespondenceAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(CorrespondenceAttachmentsInner.to_json())

# convert the object into a dict
correspondence_attachments_inner_dict = correspondence_attachments_inner_instance.to_dict()
# create an instance of CorrespondenceAttachmentsInner from a dict
correspondence_attachments_inner_from_dict = CorrespondenceAttachmentsInner.from_dict(correspondence_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


