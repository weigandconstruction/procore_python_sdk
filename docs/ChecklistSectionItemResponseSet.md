# ChecklistSectionItemResponseSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the response set | [optional] 
**name** | **str** | Name of the response set | [optional] 
**responses** | [**List[ChecklistResponse]**](ChecklistResponse.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of inspection creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item_response_set import ChecklistSectionItemResponseSet

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItemResponseSet from a JSON string
checklist_section_item_response_set_instance = ChecklistSectionItemResponseSet.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItemResponseSet.to_json())

# convert the object into a dict
checklist_section_item_response_set_dict = checklist_section_item_response_set_instance.to_dict()
# create an instance of ChecklistSectionItemResponseSet from a dict
checklist_section_item_response_set_from_dict = ChecklistSectionItemResponseSet.from_dict(checklist_section_item_response_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


