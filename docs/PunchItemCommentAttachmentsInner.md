# PunchItemCommentAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Use :name, :filename to be deprecated | [optional] 
**url** | **str** |  | [optional] 
**filename** | **str** | :filename to be deprecated, use :name | [optional] 
**thumbnail_url** | **str** | thumbnail url | [optional] 

## Example

```python
from procore_sdk.models.punch_item_comment_attachments_inner import PunchItemCommentAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemCommentAttachmentsInner from a JSON string
punch_item_comment_attachments_inner_instance = PunchItemCommentAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(PunchItemCommentAttachmentsInner.to_json())

# convert the object into a dict
punch_item_comment_attachments_inner_dict = punch_item_comment_attachments_inner_instance.to_dict()
# create an instance of PunchItemCommentAttachmentsInner from a dict
punch_item_comment_attachments_inner_from_dict = PunchItemCommentAttachmentsInner.from_dict(punch_item_comment_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


