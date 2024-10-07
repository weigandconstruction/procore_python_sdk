# ChecklistTemplate5SectionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**items** | [**List[ChecklistTemplate5SectionsInnerItemsInner]**](ChecklistTemplate5SectionsInnerItemsInner.md) | Checklist Items | [optional] 

## Example

```python
from procore_sdk.models.checklist_template5_sections_inner import ChecklistTemplate5SectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate5SectionsInner from a JSON string
checklist_template5_sections_inner_instance = ChecklistTemplate5SectionsInner.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate5SectionsInner.to_json())

# convert the object into a dict
checklist_template5_sections_inner_dict = checklist_template5_sections_inner_instance.to_dict()
# create an instance of ChecklistTemplate5SectionsInner from a dict
checklist_template5_sections_inner_from_dict = ChecklistTemplate5SectionsInner.from_dict(checklist_template5_sections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


