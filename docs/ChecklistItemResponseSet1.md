# ChecklistItemResponseSet1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | The name of the Item Response Set | [optional] 
**active** | **bool** | Indicates whether an Item Response Set is available for use. | [optional] 
**created_at** | **datetime** | Represents when an Item Response Set was created | [optional] 
**updated_at** | **datetime** | Represents when a Item Response Set was last updated | [optional] 
**responses** | [**List[ChecklistResponse]**](ChecklistResponse.md) | Responses | [optional] 
**in_use** | **bool** | Indicates whether a Response Set is being used by an Inspection Template Item | [optional] 
**deletable** | **bool** | Indicates whether a Response Set is deletable. | [optional] 
**procore_standard** | **bool** | Indicates whether a Response Set is a Procore standard set. | [optional] 

## Example

```python
from procore_sdk.models.checklist_item_response_set1 import ChecklistItemResponseSet1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponseSet1 from a JSON string
checklist_item_response_set1_instance = ChecklistItemResponseSet1.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponseSet1.to_json())

# convert the object into a dict
checklist_item_response_set1_dict = checklist_item_response_set1_instance.to_dict()
# create an instance of ChecklistItemResponseSet1 from a dict
checklist_item_response_set1_from_dict = ChecklistItemResponseSet1.from_dict(checklist_item_response_set1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


