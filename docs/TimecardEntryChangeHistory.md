# TimecardEntryChangeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** | Column that changed | [optional] 
**old_value** | **str** | Column&#39;s old value | [optional] 
**new_value** | **str** | Column&#39;s new value | [optional] 
**created_at** | **str** | Created at | [optional] 
**created_by** | **str** | Created by | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry_change_history import TimecardEntryChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntryChangeHistory from a JSON string
timecard_entry_change_history_instance = TimecardEntryChangeHistory.from_json(json)
# print the JSON string representation of the object
print(TimecardEntryChangeHistory.to_json())

# convert the object into a dict
timecard_entry_change_history_dict = timecard_entry_change_history_instance.to_dict()
# create an instance of TimecardEntryChangeHistory from a dict
timecard_entry_change_history_from_dict = TimecardEntryChangeHistory.from_dict(timecard_entry_change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


