# Timesheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**var_date** | **date** | Timesheet date | [optional] 
**number** | **int** | Timesheet number | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**name** | **str** | Timesheet name | [optional] 
**status** | **str** | The approval status of the Timesheet | [optional] 
**timecard_entries** | [**List[TimesheetEntries]**](TimesheetEntries.md) |  | [optional] 

## Example

```python
from procore_sdk.models.timesheet import Timesheet

# TODO update the JSON string below
json = "{}"
# create an instance of Timesheet from a JSON string
timesheet_instance = Timesheet.from_json(json)
# print the JSON string representation of the object
print(Timesheet.to_json())

# convert the object into a dict
timesheet_dict = timesheet_instance.to_dict()
# create an instance of Timesheet from a dict
timesheet_from_dict = Timesheet.from_dict(timesheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


