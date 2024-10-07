# TimesheetChangeHistoryBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | Array of Timecard Entry IDs you want to view the Change Histories for | 

## Example

```python
from procore_sdk.models.timesheet_change_history_body import TimesheetChangeHistoryBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetChangeHistoryBody from a JSON string
timesheet_change_history_body_instance = TimesheetChangeHistoryBody.from_json(json)
# print the JSON string representation of the object
print(TimesheetChangeHistoryBody.to_json())

# convert the object into a dict
timesheet_change_history_body_dict = timesheet_change_history_body_instance.to_dict()
# create an instance of TimesheetChangeHistoryBody from a dict
timesheet_change_history_body_from_dict = TimesheetChangeHistoryBody.from_dict(timesheet_change_history_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


