# TimeAndMaterialTimecardBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_timecard** | [**TimeAndMaterialTimecardProperties**](TimeAndMaterialTimecardProperties.md) |  | 

## Example

```python
from procore_sdk.models.time_and_material_timecard_body import TimeAndMaterialTimecardBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialTimecardBody from a JSON string
time_and_material_timecard_body_instance = TimeAndMaterialTimecardBody.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialTimecardBody.to_json())

# convert the object into a dict
time_and_material_timecard_body_dict = time_and_material_timecard_body_instance.to_dict()
# create an instance of TimeAndMaterialTimecardBody from a dict
time_and_material_timecard_body_from_dict = TimeAndMaterialTimecardBody.from_dict(time_and_material_timecard_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


