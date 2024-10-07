# ChecklistTemplateSectionSyncedTo

Checklist Template's synced Company Template information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | [optional] 
**list_template_id** | **int** | Company Checklist Template ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_template_section_synced_to import ChecklistTemplateSectionSyncedTo

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplateSectionSyncedTo from a JSON string
checklist_template_section_synced_to_instance = ChecklistTemplateSectionSyncedTo.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplateSectionSyncedTo.to_json())

# convert the object into a dict
checklist_template_section_synced_to_dict = checklist_template_section_synced_to_instance.to_dict()
# create an instance of ChecklistTemplateSectionSyncedTo from a dict
checklist_template_section_synced_to_from_dict = ChecklistTemplateSectionSyncedTo.from_dict(checklist_template_section_synced_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


