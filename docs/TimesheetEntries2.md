# TimesheetEntries2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Timesheet entry date | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**hours** | **str** | Total number of hours the resource was on sight. | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**time_in** | **datetime** | Starting time for the Timesheet | [optional] 
**time_out** | **datetime** | Ending time for the Timesheet | [optional] 
**injured** | **bool** | Injury status | [optional] 
**lunch_time** | **int** | Lunch duration | [optional] 
**billable** | **bool** | Billable status | [optional] 
**origin_id** | **int** | ID of related external data | [optional] 
**origin_data** | **str** | Value of related external data | [optional] 
**crew** | [**TimesheetEntriesCrew**](TimesheetEntriesCrew.md) |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**timecard_time_type** | [**TimecardTimeType2**](TimecardTimeType2.md) |  | [optional] 

## Example

```python
from procore_sdk.models.timesheet_entries2 import TimesheetEntries2

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetEntries2 from a JSON string
timesheet_entries2_instance = TimesheetEntries2.from_json(json)
# print the JSON string representation of the object
print(TimesheetEntries2.to_json())

# convert the object into a dict
timesheet_entries2_dict = timesheet_entries2_instance.to_dict()
# create an instance of TimesheetEntries2 from a dict
timesheet_entries2_from_dict = TimesheetEntries2.from_dict(timesheet_entries2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


