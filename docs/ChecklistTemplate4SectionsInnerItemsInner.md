# ChecklistTemplate4SectionsInnerItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**status** | **str** | Status | [optional] 
**section_id** | **int** | Checklist Section ID | [optional] 
**section_position** | **int** | Checklist Section Position | [optional] 
**position** | **int** | Position | [optional] 

## Example

```python
from procore_sdk.models.checklist_template4_sections_inner_items_inner import ChecklistTemplate4SectionsInnerItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate4SectionsInnerItemsInner from a JSON string
checklist_template4_sections_inner_items_inner_instance = ChecklistTemplate4SectionsInnerItemsInner.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate4SectionsInnerItemsInner.to_json())

# convert the object into a dict
checklist_template4_sections_inner_items_inner_dict = checklist_template4_sections_inner_items_inner_instance.to_dict()
# create an instance of ChecklistTemplate4SectionsInnerItemsInner from a dict
checklist_template4_sections_inner_items_inner_from_dict = ChecklistTemplate4SectionsInnerItemsInner.from_dict(checklist_template4_sections_inner_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


