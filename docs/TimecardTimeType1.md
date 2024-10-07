# TimecardTimeType1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Time type id | [optional] 
**time_type** | **str** | Time type | [optional] 
**abbreviated_time_type** | **str** | Time type abbreviated | [optional] 
**var_global** | **bool** | Time type global status | [optional] 

## Example

```python
from procore_sdk.models.timecard_time_type1 import TimecardTimeType1

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardTimeType1 from a JSON string
timecard_time_type1_instance = TimecardTimeType1.from_json(json)
# print the JSON string representation of the object
print(TimecardTimeType1.to_json())

# convert the object into a dict
timecard_time_type1_dict = timecard_time_type1_instance.to_dict()
# create an instance of TimecardTimeType1 from a dict
timecard_time_type1_from_dict = TimecardTimeType1.from_dict(timecard_time_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


