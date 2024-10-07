# RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest1DailyConstructionReportLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apprentice_hours** | **str** | Number of hours that the Apprentice workers were on site | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**first_year_hours** | **str** | Number of hours performed by first-year apprentices | [optional] 
**foreman_hours** | **str** | Number of hours that the foremen were on site | [optional] 
**journeyman_hours** | **str** | Number of hours that the journeymen were on site | [optional] 
**local_city_hours** | **str** | Number of hours performed by local city resident workers | [optional] 
**local_county_hours** | **str** | Number of hours performecd by local county resident workers | [optional] 
**minority_hours** | **str** | Number of hours performed by minority workers | [optional] 
**notes** | **str** | Additional notes | [optional] 
**number_of_apprentice_workers** | **int** | Number of apprentice workers on site | [optional] 
**number_of_foreman_workers** | **int** | Number of foremen on site | [optional] 
**number_of_journeyman_workers** | **int** | Number of journeymen on site | [optional] 
**number_of_other_workers** | **int** | Number of other workers on site | [optional] 
**other_hours** | **str** | Number of hours that other workers were on site | [optional] 
**vendor_id** | **int** | ID of the Vendor associated to the report | 
**veteran_hours** | **str** | Number of hours performed by veteran workers | [optional] 
**women_hours** | **str** | Number of hours performed by women workers | [optional] 
**trade_id** | **int** | ID of the Trade associated to the report | 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_construction_report_logs_post_request1_daily_construction_report_log import RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest1DailyConstructionReportLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest1DailyConstructionReportLog from a JSON string
rest_v10_projects_project_id_daily_construction_report_logs_post_request1_daily_construction_report_log_instance = RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest1DailyConstructionReportLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest1DailyConstructionReportLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_construction_report_logs_post_request1_daily_construction_report_log_dict = rest_v10_projects_project_id_daily_construction_report_logs_post_request1_daily_construction_report_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest1DailyConstructionReportLog from a dict
rest_v10_projects_project_id_daily_construction_report_logs_post_request1_daily_construction_report_log_from_dict = RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest1DailyConstructionReportLog.from_dict(rest_v10_projects_project_id_daily_construction_report_logs_post_request1_daily_construction_report_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


