# ChecklistInspectionItemObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**checklist_item_id** | **int** | Checklist Item ID | [optional] 
**checklist_list_id** | **int** | Checklist List ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**created_by** | [**RestV11RequisitionsGet200ResponseInnerCreatedBy**](RestV11RequisitionsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_inspection_item_observation import ChecklistInspectionItemObservation

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistInspectionItemObservation from a JSON string
checklist_inspection_item_observation_instance = ChecklistInspectionItemObservation.from_json(json)
# print the JSON string representation of the object
print(ChecklistInspectionItemObservation.to_json())

# convert the object into a dict
checklist_inspection_item_observation_dict = checklist_inspection_item_observation_instance.to_dict()
# create an instance of ChecklistInspectionItemObservation from a dict
checklist_inspection_item_observation_from_dict = ChecklistInspectionItemObservation.from_dict(checklist_inspection_item_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


