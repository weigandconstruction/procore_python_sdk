# ChecklistSectionItemObservationsInnerType

Observation Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**active** | **bool** | Observation Type active flag | [optional] 

## Example

```python
from procore_sdk.models.checklist_section_item_observations_inner_type import ChecklistSectionItemObservationsInnerType

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSectionItemObservationsInnerType from a JSON string
checklist_section_item_observations_inner_type_instance = ChecklistSectionItemObservationsInnerType.from_json(json)
# print the JSON string representation of the object
print(ChecklistSectionItemObservationsInnerType.to_json())

# convert the object into a dict
checklist_section_item_observations_inner_type_dict = checklist_section_item_observations_inner_type_instance.to_dict()
# create an instance of ChecklistSectionItemObservationsInnerType from a dict
checklist_section_item_observations_inner_type_from_dict = ChecklistSectionItemObservationsInnerType.from_dict(checklist_section_item_observations_inner_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


