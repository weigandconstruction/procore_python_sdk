# ChecklistTemplateItemType

Checklist Item Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Checklist Item Type ID | [optional] 
**category** | **str** | Checklist Item Type Category | [optional] 
**name** | **str** | Checklist Item Type Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_template_item_type import ChecklistTemplateItemType

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplateItemType from a JSON string
checklist_template_item_type_instance = ChecklistTemplateItemType.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplateItemType.to_json())

# convert the object into a dict
checklist_template_item_type_dict = checklist_template_item_type_instance.to_dict()
# create an instance of ChecklistTemplateItemType from a dict
checklist_template_item_type_from_dict = ChecklistTemplateItemType.from_dict(checklist_template_item_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


