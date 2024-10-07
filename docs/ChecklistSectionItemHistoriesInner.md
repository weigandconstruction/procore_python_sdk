# ChecklistSectionItemHistoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**body** | **str** | Text describing the status change | [optional] 
**status** | **str** |  | [optional] 
**responded_with** | **str** | Name of Response at time of inspection | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item_histories_inner import ChecklistSectionItemHistoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItemHistoriesInner from a JSON string
checklist_section_item_histories_inner_instance = ChecklistSectionItemHistoriesInner.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItemHistoriesInner.to_json())

# convert the object into a dict
checklist_section_item_histories_inner_dict = checklist_section_item_histories_inner_instance.to_dict()
# create an instance of ChecklistSectionItemHistoriesInner from a dict
checklist_section_item_histories_inner_from_dict = ChecklistSectionItemHistoriesInner.from_dict(checklist_section_item_histories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


