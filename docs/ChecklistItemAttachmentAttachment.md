# ChecklistItemAttachmentAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | URL | [optional] 
**filename** | **str** | Filename | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_attachment_attachment import ChecklistItemAttachmentAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemAttachmentAttachment from a JSON string
checklist_item_attachment_attachment_instance = ChecklistItemAttachmentAttachment.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemAttachmentAttachment.to_json())

# convert the object into a dict
checklist_item_attachment_attachment_dict = checklist_item_attachment_attachment_instance.to_dict()
# create an instance of ChecklistItemAttachmentAttachment from a dict
checklist_item_attachment_attachment_from_dict = ChecklistItemAttachmentAttachment.from_dict(checklist_item_attachment_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


