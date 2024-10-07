# ChecklistScheduleAttachmentAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File ID | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**content_type** | **str** | A mime type or a file extension | [optional] 
**thumbnail_url** | **str** | Image Thumbnail URL | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 
**filename** | **str** | Base name of the file without its path | [optional] 
**viewable_document_id** | **int** | Viewable document ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_schedule_attachment_attachment import ChecklistScheduleAttachmentAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistScheduleAttachmentAttachment from a JSON string
checklist_schedule_attachment_attachment_instance = ChecklistScheduleAttachmentAttachment.from_json(json)
# print the JSON string representation of the object
print(ChecklistScheduleAttachmentAttachment.to_json())

# convert the object into a dict
checklist_schedule_attachment_attachment_dict = checklist_schedule_attachment_attachment_instance.to_dict()
# create an instance of ChecklistScheduleAttachmentAttachment from a dict
checklist_schedule_attachment_attachment_from_dict = ChecklistScheduleAttachmentAttachment.from_dict(checklist_schedule_attachment_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


