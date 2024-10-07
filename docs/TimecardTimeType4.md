# TimecardTimeType4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Time type id | [optional] 
**time_type** | **str** | Time type | [optional] 

## Example

```python
from procore_sdk.models.timecard_time_type4 import TimecardTimeType4

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardTimeType4 from a JSON string
timecard_time_type4_instance = TimecardTimeType4.from_json(json)
# print the JSON string representation of the object
print(TimecardTimeType4.to_json())

# convert the object into a dict
timecard_time_type4_dict = timecard_time_type4_instance.to_dict()
# create an instance of TimecardTimeType4 from a dict
timecard_time_type4_from_dict = TimecardTimeType4.from_dict(timecard_time_type4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


