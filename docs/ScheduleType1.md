# ScheduleType1

Schedule Type object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The Key of the Schedule Type | 
**p6_id** | **str** | The Primavera P6 Identifier of the Schedule Type | [optional] 

## Example

```python
from procore_sdk.models.schedule_type1 import ScheduleType1

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleType1 from a JSON string
schedule_type1_instance = ScheduleType1.from_json(json)
# print the JSON string representation of the object
print(ScheduleType1.to_json())

# convert the object into a dict
schedule_type1_dict = schedule_type1_instance.to_dict()
# create an instance of ScheduleType1 from a dict
schedule_type1_from_dict = ScheduleType1.from_dict(schedule_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


