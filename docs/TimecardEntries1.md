# TimecardEntries1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_status** | **str** | Approval status of a Timecard Entry | [optional] 
**billable** | **bool** | The Billable status of the Timecard Entry | [optional] [default to False]
**cost_code_id** | **int** | The ID of the Cost Code of the Timecard Entry | [optional] 
**crew_id** | **int** | The ID of the crew for the Timecard Entry | [optional] 
**var_date** | **date** | The Date of the Timecard Entry | [optional] 
**description** | **str** | The description of the Timecard Entry | [optional] 
**hours** | **int** | Hours worked on a Timecard Entry | [optional] 
**location_id** | **int** | The location ID for the Timecard Entry | [optional] 
**origin_id** | **int** | ID of related external data | [optional] 
**origin_data** | **str** | Value of related external data | [optional] 
**party_id** | **int** | The ID of the party for the Timecard Entry | [optional] 
**project_id** | **int** | The ID of the Timecard Time Type of the Timecard Entry | [optional] 
**set_timecard_time_type_automatically** | **bool** | Whether or not to allow the automatic overtime management system to apply the configured rules to set the timecard_time_type_id and/or split the timecard entry automatically | [optional] 
**sub_job_id** | **int** | The ID of the Sub Job of the Timecard Entry | [optional] 
**time_in** | **datetime** | Time in for the Timecard Entry | [optional] 
**time_out** | **datetime** | Time out for the Timecard Entry | [optional] 
**timesheet_id** | **int** | The ID of the Timesheet of the Timecard Entry | [optional] 
**timecard_time_type_id** | **int** | The ID of the Timecard Time Type of the Timecard Entry | [optional] 
**updates** | [**List[TimecardEntries1UpdatesInner]**](TimecardEntries1UpdatesInner.md) | The IDs of the timecards you want to update | 
**user_id** | **int** | The ID of the Login Information of the Timecard Entry | [optional] 
**work_classification_id** | **int** | The ID of the Work Classification of the Timecard Entry | [optional] 

## Example

```python
from procore_sdk.models.timecard_entries1 import TimecardEntries1

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntries1 from a JSON string
timecard_entries1_instance = TimecardEntries1.from_json(json)
# print the JSON string representation of the object
print(TimecardEntries1.to_json())

# convert the object into a dict
timecard_entries1_dict = timecard_entries1_instance.to_dict()
# create an instance of TimecardEntries1 from a dict
timecard_entries1_from_dict = TimecardEntries1.from_dict(timecard_entries1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


