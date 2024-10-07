# Timesheet1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party** | [**Party**](Party.md) |  | [optional] 
**other_hours** | [**List[OtherHours]**](OtherHours.md) |  | [optional] 
**timecard_entries** | [**List[TimecardEntry1]**](TimecardEntry1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.timesheet1 import Timesheet1

# TODO update the JSON string below
json = "{}"
# create an instance of Timesheet1 from a JSON string
timesheet1_instance = Timesheet1.from_json(json)
# print the JSON string representation of the object
print(Timesheet1.to_json())

# convert the object into a dict
timesheet1_dict = timesheet1_instance.to_dict()
# create an instance of Timesheet1 from a dict
timesheet1_from_dict = Timesheet1.from_dict(timesheet1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


