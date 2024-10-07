# VendorCommentAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**content_type** | **str** | A mime type or a file extension | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 

## Example

```python
from procore_sdk.models.vendor_comment_attachments_inner import VendorCommentAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VendorCommentAttachmentsInner from a JSON string
vendor_comment_attachments_inner_instance = VendorCommentAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(VendorCommentAttachmentsInner.to_json())

# convert the object into a dict
vendor_comment_attachments_inner_dict = vendor_comment_attachments_inner_instance.to_dict()
# create an instance of VendorCommentAttachmentsInner from a dict
vendor_comment_attachments_inner_from_dict = VendorCommentAttachmentsInner.from_dict(vendor_comment_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


