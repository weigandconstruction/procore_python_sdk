# ScheduleType

Schedule Type object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The Key of the Schedule Type | [optional] 
**p6_id** | **str** | The Primavera P6 Identifier of the Schedule Type | [optional] 

## Example

```python
from procore_sdk.models.schedule_type import ScheduleType

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleType from a JSON string
schedule_type_instance = ScheduleType.from_json(json)
# print the JSON string representation of the object
print(ScheduleType.to_json())

# convert the object into a dict
schedule_type_dict = schedule_type_instance.to_dict()
# create an instance of ScheduleType from a dict
schedule_type_from_dict = ScheduleType.from_dict(schedule_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


