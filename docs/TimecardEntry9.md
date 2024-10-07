# TimecardEntry9

Timecard Entry object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **str** | Total number of hours worked (excluding breaks) for the timecard entry. This property is not required if the timesheet time entry is configured for start time and stop time. | 
**lunch_time** | **str** | The duration of the lunch break, in minutes, for the timecard entry. This property is only required if the timesheet time entry is configured for start time and stop time. | 
**party_id** | **int** | The ID of the Party of the Timecard Entry | [optional] 
**time_in** | **str** | The start time of the timecard entry in ISO 8601 format. This property is only required if the timesheet time entry is configured for start time and stop time. | 
**time_out** | **str** | The stop time of the timecard entry in ISO 8601 format. This property is only required if the timesheet time entry is configured for start time and stop time. | 
**billable** | **bool** | The billable status of the timecard entry. Must be either true or false. | [optional] [default to False]
**var_date** | **date** | The date of the timecard entry in ISO 8601 format. | [optional] 
**datetime** | **datetime** | The date and time value of record. This property is mutually exclusive with the Date property. | [optional] 
**description** | **str** | The description of the timecard entry. | [optional] 
**timecard_time_type_id** | **int** | The ID of the timecard time type corresponding to the timecard entry property. | [optional] 
**timesheet_id** | **int** | The ID of the timesheet corresponding to the timecard entry property. | [optional] 
**cost_code_id** | **int** | The ID of the cost code corresponding to the timecard entry property. | [optional] 
**sub_job_id** | **int** | The ID of the subjob corresponding to the timecard entry property. | [optional] 
**location_id** | **int** | The ID of the multi-tier location corresponding to the timecard entry property. | [optional] 
**login_information_id** | **int** | The ID of the login information corresponding to the timecard entry property. | [optional] 
**origin_id** | **int** | The ID of the related external data. | [optional] 
**origin_data** | **str** | The value of the related external data. | [optional] 
**line_item_type_id** | **int** | The ID of the line item type corresponding to the time card entry. | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry9 import TimecardEntry9

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry9 from a JSON string
timecard_entry9_instance = TimecardEntry9.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry9.to_json())

# convert the object into a dict
timecard_entry9_dict = timecard_entry9_instance.to_dict()
# create an instance of TimecardEntry9 from a dict
timecard_entry9_from_dict = TimecardEntry9.from_dict(timecard_entry9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


