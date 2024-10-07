# ChecklistItemAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attachment ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**created_by** | [**ChecklistCommentCreatedBy**](ChecklistCommentCreatedBy.md) |  | [optional] 
**attachment** | [**ChecklistItemAttachmentAttachment**](ChecklistItemAttachmentAttachment.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_attachment import ChecklistItemAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemAttachment from a JSON string
checklist_item_attachment_instance = ChecklistItemAttachment.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemAttachment.to_json())

# convert the object into a dict
checklist_item_attachment_dict = checklist_item_attachment_instance.to_dict()
# create an instance of ChecklistItemAttachment from a dict
checklist_item_attachment_from_dict = ChecklistItemAttachment.from_dict(checklist_item_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


