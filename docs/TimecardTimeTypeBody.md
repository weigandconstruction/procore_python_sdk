# TimecardTimeTypeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timecard_time_type** | [**TimeAndMaterialEntry**](TimeAndMaterialEntry.md) |  | 

## Example

```python
from procore_sdk.models.timecard_time_type_body import TimecardTimeTypeBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardTimeTypeBody from a JSON string
timecard_time_type_body_instance = TimecardTimeTypeBody.from_json(json)
# print the JSON string representation of the object
print(TimecardTimeTypeBody.to_json())

# convert the object into a dict
timecard_time_type_body_dict = timecard_time_type_body_instance.to_dict()
# create an instance of TimecardTimeTypeBody from a dict
timecard_time_type_body_from_dict = TimecardTimeTypeBody.from_dict(timecard_time_type_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


