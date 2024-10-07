# RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**comment** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by_collaborator** | **bool** |  | [optional] 
**custom_fields** | **object** |  | [optional] 
**var_date** | **date** |  | [optional] 
**datetime** | **datetime** |  | [optional] 
**daily_log_header_id** | **float** |  | [optional] 
**deleted_at** | **str** |  | [optional] 
**is_issue_day** | **str** |  | [optional] 
**permissions** | [**RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLogPermissions**](RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLogPermissions.md) |  | [optional] 
**position** | **float** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**attachments** | **List[object]** |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLogCreatedBy**](RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLogCreatedBy.md) |  | [optional] 
**location** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_clones_post201_response_notes_log import RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLog from a JSON string
rest_v10_projects_project_id_daily_logs_clones_post201_response_notes_log_instance = RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_logs_clones_post201_response_notes_log_dict = rest_v10_projects_project_id_daily_logs_clones_post201_response_notes_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLog from a dict
rest_v10_projects_project_id_daily_logs_clones_post201_response_notes_log_from_dict = RestV10ProjectsProjectIdDailyLogsClonesPost201ResponseNotesLog.from_dict(rest_v10_projects_project_id_daily_logs_clones_post201_response_notes_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


