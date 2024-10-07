# RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**apprentice_hours** | **str** | Number of hours the apprentice workers were on site | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date of the report | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**first_year_hours** | **str** | Number of hours performed by first-year apprentices | [optional] 
**foreman_hours** | **str** | Number of hours that the foremen were on site | [optional] 
**journeyman_hours** | **str** | Number of hours that the journeymen were on site | [optional] 
**local_city_hours** | **str** | Number of hours performed by local city resident workers | [optional] 
**local_county_hours** | **str** | Number of hours performed by local county resident workers | [optional] 
**minority_hours** | **str** | Number of hours performed by minority workers | [optional] 
**notes** | **str** | Additional notes | [optional] 
**number_of_apprentice_workers** | **int** | Number of apprentice workers on site | [optional] 
**number_of_foreman_workers** | **int** | Number of foremen on site | [optional] 
**number_of_journeyman_workers** | **int** | Number of journeymen on site | [optional] 
**number_of_other_workers** | **int** | Number of other workers on site | [optional] 
**other_hours** | **str** | Number of hours that the other worker were on site | [optional] 
**position** | **int** | Position in the list Daily Construction Reports | [optional] 
**status** | **str** | Is a log pending or approved | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**veteran_hours** | **str** | Number of hours performed by veteran workers | [optional] 
**women_hours** | **str** | Number of hours performed by women workers | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**vendor** | [**Compact**](Compact.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**permissions** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerPermissions.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner import RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner_instance = RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner_dict = rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


