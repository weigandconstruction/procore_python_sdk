# ChecklistSectionItemCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**body** | **str** | Comment body | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item_comments_inner import ChecklistSectionItemCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItemCommentsInner from a JSON string
checklist_section_item_comments_inner_instance = ChecklistSectionItemCommentsInner.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItemCommentsInner.to_json())

# convert the object into a dict
checklist_section_item_comments_inner_dict = checklist_section_item_comments_inner_instance.to_dict()
# create an instance of ChecklistSectionItemCommentsInner from a dict
checklist_section_item_comments_inner_from_dict = ChecklistSectionItemCommentsInner.from_dict(checklist_section_item_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


