# ChecklistSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**origin_id** | **int** | ID of Corresponding Checklist Template Section | [optional] 
**items** | [**List[ChecklistSectionItem]**](ChecklistSectionItem.md) | Checklist Items | [optional] 
**template_section_id** | **int** | Template Section ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_section import ChecklistSection

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSection from a JSON string
checklist_section_instance = ChecklistSection.from_json(json)
# print the JSON string representation of the object
print(ChecklistSection.to_json())

# convert the object into a dict
checklist_section_dict = checklist_section_instance.to_dict()
# create an instance of ChecklistSection from a dict
checklist_section_from_dict = ChecklistSection.from_dict(checklist_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


