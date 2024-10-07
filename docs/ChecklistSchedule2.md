# ChecklistSchedule2

Checklist Schedule object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the Checklist Schedule. | [optional] 
**first_inspection_due_at** | **datetime** | Timestamp indicating when the first Inspection in the Schedule should be due. Cannot be in the past. | [optional] 
**ends_at** | **datetime** | Timestamp indicating when the last Inspection in the Schedule should be due. Not used when frequency is once. | [optional] 
**frequency** | **str** | The frequency at which Inspections will be created by the Schedule. | [optional] 
**location_id** | **int** | The ID of the Location to set on the Schedule. | [optional] 
**point_of_contact_id** | **int** | The ID of a User to be set as the of the point of contact on the Schedule | [optional] 
**responsible_contractor_id** | **int** | The ID of a vendor to set as the responsible contractor on the Schedule. | [optional] 
**specification_section_id** | **int** | The ID of the specification section to set on the Schedule. | [optional] 
**assignee_ids** | **List[int]** |  | [optional] 
**distribution_member_ids** | **List[int]** |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_schedule2 import ChecklistSchedule2

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSchedule2 from a JSON string
checklist_schedule2_instance = ChecklistSchedule2.from_json(json)
# print the JSON string representation of the object
print(ChecklistSchedule2.to_json())

# convert the object into a dict
checklist_schedule2_dict = checklist_schedule2_instance.to_dict()
# create an instance of ChecklistSchedule2 from a dict
checklist_schedule2_from_dict = ChecklistSchedule2.from_dict(checklist_schedule2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


