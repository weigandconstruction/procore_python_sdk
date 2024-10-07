# RestV10ProjectsProjectIdTimesheetsChangeHistoryGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Change History ID | [optional] 
**ref_id** | **int** | Timesheet ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**column** | **str** | Column that changed value | [optional] 
**old_value** | **str** | Old value in the column | [optional] 
**new_value** | **str** | New value in the column | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_timesheets_change_history_get200_response_inner import RestV10ProjectsProjectIdTimesheetsChangeHistoryGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimesheetsChangeHistoryGet200ResponseInner from a JSON string
rest_v10_projects_project_id_timesheets_change_history_get200_response_inner_instance = RestV10ProjectsProjectIdTimesheetsChangeHistoryGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimesheetsChangeHistoryGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_timesheets_change_history_get200_response_inner_dict = rest_v10_projects_project_id_timesheets_change_history_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimesheetsChangeHistoryGet200ResponseInner from a dict
rest_v10_projects_project_id_timesheets_change_history_get200_response_inner_from_dict = RestV10ProjectsProjectIdTimesheetsChangeHistoryGet200ResponseInner.from_dict(rest_v10_projects_project_id_timesheets_change_history_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


