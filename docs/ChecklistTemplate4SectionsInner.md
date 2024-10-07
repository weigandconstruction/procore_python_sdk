# ChecklistTemplate4SectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**items** | [**List[ChecklistTemplate4SectionsInnerItemsInner]**](ChecklistTemplate4SectionsInnerItemsInner.md) | Checklist Items | [optional] 

## Example

```python
from procore_sdk.models.checklist_template4_sections_inner import ChecklistTemplate4SectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate4SectionsInner from a JSON string
checklist_template4_sections_inner_instance = ChecklistTemplate4SectionsInner.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate4SectionsInner.to_json())

# convert the object into a dict
checklist_template4_sections_inner_dict = checklist_template4_sections_inner_instance.to_dict()
# create an instance of ChecklistTemplate4SectionsInner from a dict
checklist_template4_sections_inner_from_dict = ChecklistTemplate4SectionsInner.from_dict(checklist_template4_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


