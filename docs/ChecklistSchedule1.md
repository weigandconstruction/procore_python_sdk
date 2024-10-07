# ChecklistSchedule1

Checklist Schedule object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the Checklist Schedule. | [optional] 
**days_created_before_due_date** | **int** | The number of days an Inspection is to be created before the due date | [optional] 
**inspection_template_id** | **int** | The ID of the Inspection Template to create the Schedule from. | [optional] 
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
from procore_sdk.models.checklist_schedule1 import ChecklistSchedule1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSchedule1 from a JSON string
checklist_schedule1_instance = ChecklistSchedule1.from_json(json)
# print the JSON string representation of the object
print(ChecklistSchedule1.to_json())

# convert the object into a dict
checklist_schedule1_dict = checklist_schedule1_instance.to_dict()
# create an instance of ChecklistSchedule1 from a dict
checklist_schedule1_from_dict = ChecklistSchedule1.from_dict(checklist_schedule1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


