# ChecklistSectionItem1AttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attachment ID | [optional] 
**url** | **str** | Attachment URL | [optional] 
**filename** | **str** | Attachment filename | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item1_attachments_inner import ChecklistSectionItem1AttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItem1AttachmentsInner from a JSON string
checklist_section_item1_attachments_inner_instance = ChecklistSectionItem1AttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItem1AttachmentsInner.to_json())

# convert the object into a dict
checklist_section_item1_attachments_inner_dict = checklist_section_item1_attachments_inner_instance.to_dict()
# create an instance of ChecklistSectionItem1AttachmentsInner from a dict
checklist_section_item1_attachments_inner_from_dict = ChecklistSectionItem1AttachmentsInner.from_dict(checklist_section_item1_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


