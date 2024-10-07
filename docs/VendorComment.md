# VendorComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Comment ID | [optional] 
**body** | **str** | The text of the Comment | [optional] 
**created_at** | **datetime** | Comment created at | [optional] 
**rating** | **int** | 1-5 | [optional] 
**attachments** | [**List[VendorCommentAttachmentsInner]**](VendorCommentAttachmentsInner.md) | Attachments | [optional] 
**created_by** | [**VendorCommentCreatedBy**](VendorCommentCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.vendor_comment import VendorComment

# TODO update the JSON string below
json = "{}"
# create an instance of VendorComment from a JSON string
vendor_comment_instance = VendorComment.from_json(json)
# print the JSON string representation of the object
print(VendorComment.to_json())

# convert the object into a dict
vendor_comment_dict = vendor_comment_instance.to_dict()
# create an instance of VendorComment from a dict
vendor_comment_from_dict = VendorComment.from_dict(vendor_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


