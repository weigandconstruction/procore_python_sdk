# ChecklistSpecificationSection

Specification Section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**current_revision_id** | **int** | Current revision ID | [optional] 
**description** | **str** | Description | [optional] 
**section** | **str** | Number | [optional] 
**latest_revision_url** | **str** | Url to PDF view | [optional] 

## Example

```python
from procore_sdk.models.checklist_specification_section import ChecklistSpecificationSection

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSpecificationSection from a JSON string
checklist_specification_section_instance = ChecklistSpecificationSection.from_json(json)
# print the JSON string representation of the object
print(ChecklistSpecificationSection.to_json())

# convert the object into a dict
checklist_specification_section_dict = checklist_specification_section_instance.to_dict()
# create an instance of ChecklistSpecificationSection from a dict
checklist_specification_section_from_dict = ChecklistSpecificationSection.from_dict(checklist_specification_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


