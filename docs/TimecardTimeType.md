# TimecardTimeType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Time type id | [optional] 
**abbreviated_time_type** | **str** | Time type abbreviated | [optional] 
**company_id** | **int** | Time type company id | [optional] 
**var_global** | **bool** | Time type global status | [optional] 
**time_type** | **str** | Time type | [optional] 

## Example

```python
from procore_sdk.models.timecard_time_type import TimecardTimeType

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardTimeType from a JSON string
timecard_time_type_instance = TimecardTimeType.from_json(json)
# print the JSON string representation of the object
print(TimecardTimeType.to_json())

# convert the object into a dict
timecard_time_type_dict = timecard_time_type_instance.to_dict()
# create an instance of TimecardTimeType from a dict
timecard_time_type_from_dict = TimecardTimeType.from_dict(timecard_time_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


