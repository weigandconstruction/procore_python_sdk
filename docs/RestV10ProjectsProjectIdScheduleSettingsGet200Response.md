# RestV10ProjectsProjectIdScheduleSettingsGet200Response

Schedule Project Settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project | [optional] 
**company_id** | **int** | Company | [optional] 
**primavera_schedule_id** | **str** | Primavera schedule | [optional] 
**schedule_type** | **str** | Schedule type | [optional] 
**schedule_file_pattern** | **str** | Schedule file pattern | [optional] 
**project_integration** | **bool** | Project integration | [optional] 
**display_task_names_with_full_outline_path** | **bool** | Display task names with full outline path | [optional] 
**schedule_show_resources_on_calendar** | **bool** | Schedule show resources on calendar | [optional] 
**schedule_allow_task_updates** | **bool** | Schedule allow task updates | [optional] 
**schedule_task_auto_formatting** | **bool** | Schedule task auto formatting | [optional] 
**create_calendar_item_enabled** | **bool** | Create calendar item enabled | [optional] 
**calendar_people_filters_enabled** | **bool** | Calendar people filters enabled | [optional] 
**schedule_use_project_admin_working_days** | **bool** | Schedule use project admin working days | [optional] 
**email_settings** | [**RestV10ProjectsProjectIdScheduleSettingsGet200ResponseEmailSettings**](RestV10ProjectsProjectIdScheduleSettingsGet200ResponseEmailSettings.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_schedule_settings_get200_response import RestV10ProjectsProjectIdScheduleSettingsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdScheduleSettingsGet200Response from a JSON string
rest_v10_projects_project_id_schedule_settings_get200_response_instance = RestV10ProjectsProjectIdScheduleSettingsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdScheduleSettingsGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_schedule_settings_get200_response_dict = rest_v10_projects_project_id_schedule_settings_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdScheduleSettingsGet200Response from a dict
rest_v10_projects_project_id_schedule_settings_get200_response_from_dict = RestV10ProjectsProjectIdScheduleSettingsGet200Response.from_dict(rest_v10_projects_project_id_schedule_settings_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


