# ChecklistSectionItem1AttachmentHistoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attachment ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**attachment** | [**RestV10WorkOrderContractsPost201ResponseAttachmentsInner**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item1_attachment_histories_inner import ChecklistSectionItem1AttachmentHistoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItem1AttachmentHistoriesInner from a JSON string
checklist_section_item1_attachment_histories_inner_instance = ChecklistSectionItem1AttachmentHistoriesInner.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItem1AttachmentHistoriesInner.to_json())

# convert the object into a dict
checklist_section_item1_attachment_histories_inner_dict = checklist_section_item1_attachment_histories_inner_instance.to_dict()
# create an instance of ChecklistSectionItem1AttachmentHistoriesInner from a dict
checklist_section_item1_attachment_histories_inner_from_dict = ChecklistSectionItem1AttachmentHistoriesInner.from_dict(checklist_section_item1_attachment_histories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


