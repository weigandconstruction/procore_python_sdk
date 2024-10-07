# ChecklistItemResponseSet2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | The name of the Item Response Set | [optional] 
**active** | **bool** | Indicates whether an Item Response Set is available for use. | [optional] 
**created_at** | **datetime** | Represents when an Item Response Set was created | [optional] 
**updated_at** | **datetime** | Represents when a Item Response Set was last updated | [optional] 
**responses** | [**List[ChecklistResponse1]**](ChecklistResponse1.md) | Responses | [optional] 
**deletable** | **bool** | Indicates whether a Response Set is deletable. | [optional] 
**procore_standard** | **bool** | Indicates whether a Response Set is a Procore standard set. | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_response_set2 import ChecklistItemResponseSet2

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponseSet2 from a JSON string
checklist_item_response_set2_instance = ChecklistItemResponseSet2.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponseSet2.to_json())

# convert the object into a dict
checklist_item_response_set2_dict = checklist_item_response_set2_instance.to_dict()
# create an instance of ChecklistItemResponseSet2 from a dict
checklist_item_response_set2_from_dict = ChecklistItemResponseSet2.from_dict(checklist_item_response_set2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


