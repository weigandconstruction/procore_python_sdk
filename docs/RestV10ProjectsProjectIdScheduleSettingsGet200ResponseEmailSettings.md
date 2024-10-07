# RestV10ProjectsProjectIdScheduleSettingsGet200ResponseEmailSettings

Email settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_schedule_email_setting_id** | **int** | Project schedule email setting | [optional] 
**send_weekly** | **bool** | Send weekly | [optional] 
**day_of_week** | **int** | Day of week | [optional] 
**hour_to_send** | **int** | Hour to send | [optional] 
**weeks_to_show** | **int** | Weeks to show | [optional] 
**last_sent_at** | **datetime** | Last sent at | [optional] 
**next_scheduled_at** | **datetime** | Next scheduled at | [optional] 
**lookahead_send_weekly** | **bool** | Lookahead send weekly | [optional] 
**lookahead_day_of_week** | **int** | Lookahead day of week | [optional] 
**lookahead_hour_to_send** | **int** | Lookahead hour to send | [optional] 
**lookahead_last_sent_at** | **datetime** | Lookahead last sent at | [optional] 
**lookahead_next_scheduled_at** | **datetime** | Lookahead next scheduled at | [optional] 
**resource_send_weekly** | **bool** | Resource send weekly | [optional] 
**resource_day_of_week** | **int** | Resource day of week | [optional] 
**resource_hour_to_send** | **int** | Resource hour to send | [optional] 
**resource_weeks_to_show** | **int** | Resource weeks to show | [optional] 
**resource_last_sent_at** | **datetime** | Resource last sent at | [optional] 
**resource_next_scheduled_at** | **datetime** | Resource next scheduled at | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_schedule_settings_get200_response_email_settings import RestV10ProjectsProjectIdScheduleSettingsGet200ResponseEmailSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdScheduleSettingsGet200ResponseEmailSettings from a JSON string
rest_v10_projects_project_id_schedule_settings_get200_response_email_settings_instance = RestV10ProjectsProjectIdScheduleSettingsGet200ResponseEmailSettings.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdScheduleSettingsGet200ResponseEmailSettings.to_json())

# convert the object into a dict
rest_v10_projects_project_id_schedule_settings_get200_response_email_settings_dict = rest_v10_projects_project_id_schedule_settings_get200_response_email_settings_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdScheduleSettingsGet200ResponseEmailSettings from a dict
rest_v10_projects_project_id_schedule_settings_get200_response_email_settings_from_dict = RestV10ProjectsProjectIdScheduleSettingsGet200ResponseEmailSettings.from_dict(rest_v10_projects_project_id_schedule_settings_get200_response_email_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


