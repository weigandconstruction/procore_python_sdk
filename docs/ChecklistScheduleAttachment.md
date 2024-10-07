# ChecklistScheduleAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attachment ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**schedule_id** | **int** | Checklist Schedule ID associated with attachment | [optional] 
**attachment** | [**ChecklistScheduleAttachmentAttachment**](ChecklistScheduleAttachmentAttachment.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_schedule_attachment import ChecklistScheduleAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistScheduleAttachment from a JSON string
checklist_schedule_attachment_instance = ChecklistScheduleAttachment.from_json(json)
# print the JSON string representation of the object
print(ChecklistScheduleAttachment.to_json())

# convert the object into a dict
checklist_schedule_attachment_dict = checklist_schedule_attachment_instance.to_dict()
# create an instance of ChecklistScheduleAttachment from a dict
checklist_schedule_attachment_from_dict = ChecklistScheduleAttachment.from_dict(checklist_schedule_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


