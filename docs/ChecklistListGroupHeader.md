# ChecklistListGroupHeader

Inspection Template information for grouping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Inspection Template ID | [optional] 
**name** | **str** | Inspection Template Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_list_group_header import ChecklistListGroupHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistListGroupHeader from a JSON string
checklist_list_group_header_instance = ChecklistListGroupHeader.from_json(json)
# print the JSON string representation of the object
print(ChecklistListGroupHeader.to_json())

# convert the object into a dict
checklist_list_group_header_dict = checklist_list_group_header_instance.to_dict()
# create an instance of ChecklistListGroupHeader from a dict
checklist_list_group_header_from_dict = ChecklistListGroupHeader.from_dict(checklist_list_group_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


