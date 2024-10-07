# ChecklistSectionItemObservationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**number** | **str** | Number | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**type** | [**ChecklistSectionItemObservationsInnerType**](ChecklistSectionItemObservationsInnerType.md) |  | [optional] 
**assignee** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item_observations_inner import ChecklistSectionItemObservationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItemObservationsInner from a JSON string
checklist_section_item_observations_inner_instance = ChecklistSectionItemObservationsInner.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItemObservationsInner.to_json())

# convert the object into a dict
checklist_section_item_observations_inner_dict = checklist_section_item_observations_inner_instance.to_dict()
# create an instance of ChecklistSectionItemObservationsInner from a dict
checklist_section_item_observations_inner_from_dict = ChecklistSectionItemObservationsInner.from_dict(checklist_section_item_observations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


