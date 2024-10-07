# RestV10CompanyConfigurationGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strict_file_uploading** | **bool** | Strict File Uploading Allowed | [optional] 
**enable_image_real_time_as_builts** | **bool** | Image Real Time As Builts Enabled | [optional] 
**currency_symbol** | **str** | Currency Symbol | [optional] 
**currency_display** | **str** | Currency Display | [optional] 
**currency_iso_code** | **str** | Currency ISO Code | [optional] 
**timecard_employees_see_all_projects** | **bool** | Timecard Employees Can See All Projects | [optional] 
**timesheet_enabled_cost_type** | **List[int]** | Timesheet IDs With Enabled Cost Type | [optional] 
**timesheet_type** | **List[int]** | Timesheet IDs With Enabled Cost Type | [optional] 
**enable_sd_storage** | **bool** | SD Storage Enabled | [optional] 
**timesheets_custom_signature_text** | **str** | Timesheets Custom Signature Text | [optional] 
**timesheets_week_start_day** | **int** | Timesheets Week Starting Day | [optional] 
**use_24_hour_mode** | **bool** | Use 24 Hour Clock | [optional] 
**timesheets_tab_enabled** | **bool** | Timesheets Tab Enabled | [optional] 
**timecard_should_track_location** | **List[int]** | Projects whose configuration has track_timecard_location equals to true | [optional] 
**projects_timecard_in_out_enabled** | **List[int]** | Projects Timecard In Out Enabled | [optional] 
**rounding_configuration** | [**RestV10CompanyConfigurationGet200ResponseRoundingConfiguration**](RestV10CompanyConfigurationGet200ResponseRoundingConfiguration.md) |  | [optional] 
**time_and_materials_company_config** | [**RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig**](RestV10CompanyConfigurationGet200ResponseTimeAndMaterialsCompanyConfig.md) |  | [optional] 
**projects_timecard_default_lunch_time** | [**List[RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultLunchTimeInner]**](RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultLunchTimeInner.md) | Project Configurations whose timecard_default_lunch_time is not nil | [optional] 
**projects_timecard_default_start_time** | [**List[RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner]**](RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStartTimeInner.md) | Project Configurations whose timecard_default_start_time is not nil | [optional] 
**projects_timecard_default_stop_time** | [**List[RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner]**](RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner.md) | Project Configurations whose timecard_default_stop_time is not nil | [optional] 
**projects_timecard_lunch_time_tracking** | [**List[RestV10CompanyConfigurationGet200ResponseProjectsTimecardLunchTimeTrackingInner]**](RestV10CompanyConfigurationGet200ResponseProjectsTimecardLunchTimeTrackingInner.md) | Project Configurations whose timecard_lunch_time_tracking is not nil | [optional] 
**task_codes_enabled** | **bool** | Task codes enabled | [optional] 
**timecard_employees_can_select_non_budgeted_items** | **List[int]** | Timecard Employees can select non budgeted items | [optional] 
**timecards_private** | **bool** | Timecards private by default | [optional] 
**timesheet_default_cost_type_id** | **int** | Company Timesheet Budget Configuration default line item type id for non-erp integrated projects | [optional] 
**timesheet_erp_default_cost_type_id** | **int** | Company Timesheet Budget Configuration default line item type id for erp integrated projects | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_company_configuration_get200_response import RestV10CompanyConfigurationGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompanyConfigurationGet200Response from a JSON string
rest_v10_company_configuration_get200_response_instance = RestV10CompanyConfigurationGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompanyConfigurationGet200Response.to_json())

# convert the object into a dict
rest_v10_company_configuration_get200_response_dict = rest_v10_company_configuration_get200_response_instance.to_dict()
# create an instance of RestV10CompanyConfigurationGet200Response from a dict
rest_v10_company_configuration_get200_response_from_dict = RestV10CompanyConfigurationGet200Response.from_dict(rest_v10_company_configuration_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


