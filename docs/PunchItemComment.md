# PunchItemComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Punch Item Comment | [optional] 
**attachments** | [**List[PunchItemCommentAttachmentsInner]**](PunchItemCommentAttachmentsInner.md) | Punch Item Comment Attachments | [optional] 
**body** | **str** | Punch Item Comment Body | [optional] 
**created_at** | **str** | Date the Punch Item Comment was created | [optional] 
**created_by** | [**PunchItemCommentCreator**](PunchItemCommentCreator.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.punch_item_comment import PunchItemComment

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemComment from a JSON string
punch_item_comment_instance = PunchItemComment.from_json(json)
# print the JSON string representation of the object
print(PunchItemComment.to_json())

# convert the object into a dict
punch_item_comment_dict = punch_item_comment_instance.to_dict()
# create an instance of PunchItemComment from a dict
punch_item_comment_from_dict = PunchItemComment.from_dict(punch_item_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


