# ChecklistTemplate4InspectionType

Inspection Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | **datetime** | Timestamp of Inspection Type creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update to Inspection Type | [optional] 

## Example

```python
from procore_sdk.models.checklist_template4_inspection_type import ChecklistTemplate4InspectionType

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate4InspectionType from a JSON string
checklist_template4_inspection_type_instance = ChecklistTemplate4InspectionType.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate4InspectionType.to_json())

# convert the object into a dict
checklist_template4_inspection_type_dict = checklist_template4_inspection_type_instance.to_dict()
# create an instance of ChecklistTemplate4InspectionType from a dict
checklist_template4_inspection_type_from_dict = ChecklistTemplate4InspectionType.from_dict(checklist_template4_inspection_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


