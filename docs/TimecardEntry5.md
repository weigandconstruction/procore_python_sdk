# TimecardEntry5

Timecard Entry object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The Date of the Timecard Entry | 
**hours** | **str** | The Hours of the Timecard Entry | [optional] 
**lunch_time** | **str** | Duration of lunch break in minutes for the Timecard Entry. Only required if Timesheet time entry is configured for Start Time and Stop Time. | [optional] 
**time_in** | **str** | The Start Time of the Timecard Entry in ISO 8601 format. Only required if Timesheet time entry is configured for Start Time and Stop Time. | [optional] 
**time_out** | **str** | The Stop Time of the Timecard Entry in ISO 8601 format. Only required if Timesheet time entry is configured for Start Time and Stop Time. | [optional] 
**billable** | **bool** | The Billable status of the Timecard Entry | [optional] [default to False]
**description** | **str** | The Description of the Timecard Entry | [optional] 
**timecard_time_type_id** | **int** | The ID of the Timecard Time Type of the Timecard Entry | [optional] 
**location_id** | **int** | The ID of the Location of the Timecard Entry | [optional] 
**cost_code_id** | **int** | The ID of the Cost Code of the Timecard Entry | [optional] 
**set_timecard_time_type_automatically** | **bool** | Whether or not to allow the automatic overtime management system to apply the configured rules to set the timecard_time_type_id and/or split the timecard entry automatically | [optional] 
**sub_job_id** | **int** | The ID of the Sub Job of the Timecard Entry | [optional] 
**party_id** | **int** | The ID of the Party of the Timecard Entry | [optional] 
**crew_id** | **int** | The ID of the Crew of the Timecard Entry | [optional] 
**procore_signature_id** | **int** | The ID of the Procore Signature of the Timecard Entry | [optional] 
**timesheet_id** | **int** | The ID of the Timesheet of the Timecard Entry | [optional] 
**clock_in_id** | **int** | The ID of the clock in Gps Position of the Timecard Entry | [optional] 
**clock_out_id** | **int** | The ID of the clock out Gps Position of the Timecard Entry | [optional] 
**clock_in_time** | **str** | The datetime a timecard clock in was punched | [optional] 
**clock_out_time** | **str** | The datetime a timecard clock out was punched | [optional] 
**approval_status** | **str** | The Approval Status of the Timecard Entry | [optional] 
**origin_id** | **int** | ID of related external data | [optional] 
**origin_data** | **str** | Value of related external data | [optional] 
**line_item_type_id** | **int** | The ID of the Line Item Type of the Timecard Entry | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry5 import TimecardEntry5

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry5 from a JSON string
timecard_entry5_instance = TimecardEntry5.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry5.to_json())

# convert the object into a dict
timecard_entry5_dict = timecard_entry5_instance.to_dict()
# create an instance of TimecardEntry5 from a dict
timecard_entry5_from_dict = TimecardEntry5.from_dict(timecard_entry5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


