# ChecklistTemplateSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**items** | [**List[ChecklistTemplateItem]**](ChecklistTemplateItem.md) | Checklist Items | [optional] 
**synced_to** | [**ChecklistTemplateSectionSyncedTo**](ChecklistTemplateSectionSyncedTo.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_template_section import ChecklistTemplateSection

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplateSection from a JSON string
checklist_template_section_instance = ChecklistTemplateSection.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplateSection.to_json())

# convert the object into a dict
checklist_template_section_dict = checklist_template_section_instance.to_dict()
# create an instance of ChecklistTemplateSection from a dict
checklist_template_section_from_dict = ChecklistTemplateSection.from_dict(checklist_template_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


