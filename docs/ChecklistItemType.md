# ChecklistItemType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**category** | **str** | The category of the Item Type | [optional] 
**name** | **str** | The name of the Item Type | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_type import ChecklistItemType

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemType from a JSON string
checklist_item_type_instance = ChecklistItemType.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemType.to_json())

# convert the object into a dict
checklist_item_type_dict = checklist_item_type_instance.to_dict()
# create an instance of ChecklistItemType from a dict
checklist_item_type_from_dict = ChecklistItemType.from_dict(checklist_item_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


