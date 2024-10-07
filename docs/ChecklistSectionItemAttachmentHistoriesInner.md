# ChecklistSectionItemAttachmentHistoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attachment ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**attachment** | [**ChecklistSignature1Attachment**](ChecklistSignature1Attachment.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item_attachment_histories_inner import ChecklistSectionItemAttachmentHistoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItemAttachmentHistoriesInner from a JSON string
checklist_section_item_attachment_histories_inner_instance = ChecklistSectionItemAttachmentHistoriesInner.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItemAttachmentHistoriesInner.to_json())

# convert the object into a dict
checklist_section_item_attachment_histories_inner_dict = checklist_section_item_attachment_histories_inner_instance.to_dict()
# create an instance of ChecklistSectionItemAttachmentHistoriesInner from a dict
checklist_section_item_attachment_histories_inner_from_dict = ChecklistSectionItemAttachmentHistoriesInner.from_dict(checklist_section_item_attachment_histories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


