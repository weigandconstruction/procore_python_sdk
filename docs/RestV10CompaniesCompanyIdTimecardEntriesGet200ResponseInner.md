# RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Timecard entry id | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Timecard entry date | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Timecard entry description | [optional] 
**billable** | **bool** | Timecard entry billable status | [optional] 
**in_progress** | **bool** | Timecard entry in progress state | [optional] 
**hours** | **str** | Timecard entry hours | [optional] 
**time_in** | **datetime** | Timecard entry time in | [optional] 
**time_out** | **datetime** | Timecard entry time out | [optional] 
**lunch_time** | **str** | Timecard entry lunch time in minutes | [optional] 
**approval_status** | **str** | Timecard entry approval status | [optional] 
**updated_at** | **datetime** | Timecard entry updated at | [optional] 
**timecard_type** | **str** | Timecard entry time type | [optional] 
**origin_id** | **int** | ID of related external data | [optional] 
**origin_data** | **str** | Value of related external data | [optional] 
**timesheet** | [**Timesheet3**](Timesheet3.md) |  | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**sub_job** | [**TimecardEntry3SubJob**](TimecardEntry3SubJob.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**timecard_time_type** | [**TimecardTimeType**](TimecardTimeType.md) |  | [optional] 
**party** | [**Party**](Party.md) |  | [optional] 
**crew** | [**TimecardEntry3Crew**](TimecardEntry3Crew.md) |  | [optional] 
**procore_signature** | [**TimesheetsSignature**](TimesheetsSignature.md) |  | [optional] 
**project** | [**TimecardEntry3Project**](TimecardEntry3Project.md) |  | [optional] 
**clock_in** | [**TimecardEntry3ClockIn**](TimecardEntry3ClockIn.md) |  | [optional] 
**clock_out** | [**TimecardEntry3ClockIn**](TimecardEntry3ClockIn.md) |  | [optional] 
**line_item_type_id** | **int** | The ID of the Line Item Type of the Timecard Entry | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**automatically_split_timecard_entries** | [**List[TimecardEntry3]**](TimecardEntry3.md) | Timecard entries returned with associated object as part of overtime_management | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_timecard_entries_get200_response_inner import RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner from a JSON string
rest_v10_companies_company_id_timecard_entries_get200_response_inner_instance = RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_timecard_entries_get200_response_inner_dict = rest_v10_companies_company_id_timecard_entries_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner from a dict
rest_v10_companies_company_id_timecard_entries_get200_response_inner_from_dict = RestV10CompaniesCompanyIdTimecardEntriesGet200ResponseInner.from_dict(rest_v10_companies_company_id_timecard_entries_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


