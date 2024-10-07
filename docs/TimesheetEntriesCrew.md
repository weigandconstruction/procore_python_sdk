# TimesheetEntriesCrew


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of selected Crew | [optional] 
**name** | **str** | Name of selected Crew | [optional] 

## Example

```python
from procore_sdk.models.timesheet_entries_crew import TimesheetEntriesCrew

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetEntriesCrew from a JSON string
timesheet_entries_crew_instance = TimesheetEntriesCrew.from_json(json)
# print the JSON string representation of the object
print(TimesheetEntriesCrew.to_json())

# convert the object into a dict
timesheet_entries_crew_dict = timesheet_entries_crew_instance.to_dict()
# create an instance of TimesheetEntriesCrew from a dict
timesheet_entries_crew_from_dict = TimesheetEntriesCrew.from_dict(timesheet_entries_crew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


