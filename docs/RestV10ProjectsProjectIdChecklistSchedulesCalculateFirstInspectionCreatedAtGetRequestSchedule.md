# RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starts_at** | **datetime** | Schedule start date | 
**ends_at** | **datetime** | Schedule end date. When frequency is &#39;once&#39; this should be the same value as starts_at. | 
**frequency** | **str** | Schedule frequency type name | 
**days_created_before_due_date** | **int** | Number of days before the inspection due date that the inspection should be created | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request_schedule import RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule from a JSON string
rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request_schedule_instance = RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule.to_json())

# convert the object into a dict
rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request_schedule_dict = rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request_schedule_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule from a dict
rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request_schedule_from_dict = RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequestSchedule.from_dict(rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


