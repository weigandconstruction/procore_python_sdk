# TimecardEntries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timecard_entries** | [**List[TimecardEntriesTimecardEntriesInner]**](TimecardEntriesTimecardEntriesInner.md) | Array of Timecard Entries you want to create | [optional] 

## Example

```python
from procore_sdk.models.timecard_entries import TimecardEntries

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntries from a JSON string
timecard_entries_instance = TimecardEntries.from_json(json)
# print the JSON string representation of the object
print(TimecardEntries.to_json())

# convert the object into a dict
timecard_entries_dict = timecard_entries_instance.to_dict()
# create an instance of TimecardEntries from a dict
timecard_entries_from_dict = TimecardEntries.from_dict(timecard_entries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


