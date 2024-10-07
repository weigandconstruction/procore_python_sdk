# ChecklistSectionBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Section belongs to | 
**section** | [**Section**](Section.md) |  | 

## Example

```python
from procore_sdk.models.checklist_section_body import ChecklistSectionBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionBody from a JSON string
checklist_section_body_instance = ChecklistSectionBody.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionBody.to_json())

# convert the object into a dict
checklist_section_body_dict = checklist_section_body_instance.to_dict()
# create an instance of ChecklistSectionBody from a dict
checklist_section_body_from_dict = ChecklistSectionBody.from_dict(checklist_section_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


