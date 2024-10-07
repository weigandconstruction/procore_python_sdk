# ChecklistItemResponseSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | The name of the Item Response Set | [optional] 
**created_at** | **datetime** | Represents when an Item Response Set was created | [optional] 
**updated_at** | **datetime** | Represents when a Item Response Set was last updated | [optional] 
**responses** | [**List[ChecklistResponse]**](ChecklistResponse.md) | Responses | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_response_set import ChecklistItemResponseSet

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponseSet from a JSON string
checklist_item_response_set_instance = ChecklistItemResponseSet.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponseSet.to_json())

# convert the object into a dict
checklist_item_response_set_dict = checklist_item_response_set_instance.to_dict()
# create an instance of ChecklistItemResponseSet from a dict
checklist_item_response_set_from_dict = ChecklistItemResponseSet.from_dict(checklist_item_response_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


