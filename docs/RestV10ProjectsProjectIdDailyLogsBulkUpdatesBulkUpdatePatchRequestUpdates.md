# RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accident_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**call_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**delay_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**delivery_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**dumpster_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**equipment_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**inspection_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**manpower_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**daily_construction_report_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**notes_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**plan_revision_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**productivity_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**quantity_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**safety_violation_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**timecard_entry** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**visitor_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**waste_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 
**work_log** | [**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdatesAccidentLogInner.md) | Array of Update Data for Log Type | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates import RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates from a JSON string
rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_instance = RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_dict = rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates from a dict
rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_from_dict = RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequestUpdates.from_dict(rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


