# TimecardEntry8


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**billable** | **bool** | The billable status of the timecard entry. Must be either true or false. | [optional] 
**created_at** | **datetime** | The date and time when the timecard entry was created. | [optional] 
**var_date** | **date** | The date when the timecard was created. | [optional] 
**datetime** | **datetime** | The estimated UTC date time of record. | [optional] 
**deleted_at** | **datetime** | The date and time when the timecard entry was deleted. | [optional] 
**description** | **str** | The description for the timecard entry. | [optional] 
**hours** | **str** | Total number of hours the resource was on sight. | [optional] 
**timesheet_status** | **str** | Deprecated. Reference status property. | [optional] 
**approval_status** | **str** | Supervisor approval status | [optional] 
**lunch_time** | **int** | Number of hours taken for lunch | [optional] 
**time_in** | **date** | The date and time the timecard was last updated | [optional] 
**time_out** | **date** | The date and time the timecard was last updated | [optional] 
**injured** | **bool** | Whether or not an injury occured during work hours. Must be either true or false. | [optional] 
**signed** | **bool** | Whether or not the timecard has been signed. Must be either true or false. | [optional] 
**origin_id** | **int** | The ID of related external data | [optional] 
**origin_data** | **str** | The value of related external data | [optional] 
**timesheet** | [**Timesheet3**](Timesheet3.md) |  | [optional] 
**updated_at** | **datetime** | The date and time when the timesheet was updated. | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**crew** | [**TimecardEntry8Crew**](TimecardEntry8Crew.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**party** | [**Party**](Party.md) |  | [optional] 
**procore_signature** | [**TimesheetsSignature**](TimesheetsSignature.md) |  | [optional] 
**sub_job** | [**TimecardEntry3SubJob**](TimecardEntry3SubJob.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**timecard_time_type** | [**TimecardTimeType**](TimecardTimeType.md) |  | [optional] 
**line_item_type_id** | **int** | The ID of the line item type of the timecard entry | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry8 import TimecardEntry8

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry8 from a JSON string
timecard_entry8_instance = TimecardEntry8.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry8.to_json())

# convert the object into a dict
timecard_entry8_dict = timecard_entry8_instance.to_dict()
# create an instance of TimecardEntry8 from a dict
timecard_entry8_from_dict = TimecardEntry8.from_dict(timecard_entry8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


