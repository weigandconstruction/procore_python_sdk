# RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner

Schedule Calendar Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Calendar Item ID | [optional] 
**assigned** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**color** | **str** | Calendar Item color (as a hex triplet) | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**description** | **str** | Calendar Item description | [optional] 
**finish** | **date** | Calendar Item finish date | [optional] 
**full_outline_path** | **str** | ToDo full outline path (corresponds to matching field on Tasks) | [optional] 
**milestone** | **bool** | Calendar Item milestone status | [optional] 
**name** | **str** | Calendar Item name | [optional] 
**percentage** | **int** | Calendar Item completion percentage | [optional] 
**private** | **bool** | Calendar Item private status | [optional] 
**start** | **date** | Calendar Item start date | [optional] 
**task_name** | **str** | Calendar Item name (corresponds to matching field on Tasks) | [optional] 
**updated_at** | **datetime** | Calendar Item last updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner import RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner_instance = RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner_dict = rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner from a dict
rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner_from_dict = RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner.from_dict(rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


