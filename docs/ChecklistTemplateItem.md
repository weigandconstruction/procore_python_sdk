# ChecklistTemplateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**section_id** | **int** | Checklist Template Section ID | [optional] 
**details** | **str** | Details | [optional] 
**response_set** | [**ChecklistItemResponseSet**](ChecklistItemResponseSet.md) |  | [optional] 
**response_type_id** | **int** | Response Type ID | [optional] 
**type** | [**ChecklistTemplateItemType**](ChecklistTemplateItemType.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_template_item import ChecklistTemplateItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplateItem from a JSON string
checklist_template_item_instance = ChecklistTemplateItem.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplateItem.to_json())

# convert the object into a dict
checklist_template_item_dict = checklist_template_item_instance.to_dict()
# create an instance of ChecklistTemplateItem from a dict
checklist_template_item_from_dict = ChecklistTemplateItem.from_dict(checklist_template_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


