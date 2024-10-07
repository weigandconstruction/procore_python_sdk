# ChecklistSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**first_inspection_due_at** | **datetime** | Due at timestamp of first inspection | [optional] 
**ends_at** | **datetime** | Due at timestamp of last inspection | [optional] 
**next_due_at** | **datetime** | Due at timestamp of next inspection to be created | [optional] 
**frequency** | **str** | Name | [optional] 
**inspections_created** | **int** | Number of inspections created | [optional] 
**total_inspections_scheduled** | **int** | Total amount of inpections that will be created | [optional] 
**inspection_template** | [**ChecklistScheduleInspectionTemplate**](ChecklistScheduleInspectionTemplate.md) |  | [optional] 
**location_id** | **int** | Location ID | [optional] 
**assignee_ids** | **List[int]** |  | [optional] 
**point_of_contact_id** | **int** | Point of contact ID | [optional] 
**responsible_contractor_id** | **int** | ID of Vendor responsible for the work being inspected | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of update | [optional] 

## Example

```python
from procore_sdk.models.checklist_schedule import ChecklistSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistSchedule from a JSON string
checklist_schedule_instance = ChecklistSchedule.from_json(json)
# print the JSON string representation of the object
print(ChecklistSchedule.to_json())

# convert the object into a dict
checklist_schedule_dict = checklist_schedule_instance.to_dict()
# create an instance of ChecklistSchedule from a dict
checklist_schedule_from_dict = ChecklistSchedule.from_dict(checklist_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


