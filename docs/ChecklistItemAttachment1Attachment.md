# ChecklistItemAttachment1Attachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Filename | [optional] 
**content_type** | **str** |  | [optional] 
**thumbnail_url** | **str** | Thumbnail URL | [optional] 
**url** | **str** | URL | [optional] 
**filename** | **str** | Filename | [optional] 
**viewable_document_id** | **int** | Viewable Document ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_attachment1_attachment import ChecklistItemAttachment1Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemAttachment1Attachment from a JSON string
checklist_item_attachment1_attachment_instance = ChecklistItemAttachment1Attachment.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemAttachment1Attachment.to_json())

# convert the object into a dict
checklist_item_attachment1_attachment_dict = checklist_item_attachment1_attachment_instance.to_dict()
# create an instance of ChecklistItemAttachment1Attachment from a dict
checklist_item_attachment1_attachment_from_dict = ChecklistItemAttachment1Attachment.from_dict(checklist_item_attachment1_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


