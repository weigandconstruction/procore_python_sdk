# TimeAndMaterialTimecards

Time and material timecard Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_timecards_ids** | **List[int]** | Array of time and material timecard IDs specified for delete | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_timecards import TimeAndMaterialTimecards

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialTimecards from a JSON string
time_and_material_timecards_instance = TimeAndMaterialTimecards.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialTimecards.to_json())

# convert the object into a dict
time_and_material_timecards_dict = time_and_material_timecards_instance.to_dict()
# create an instance of TimeAndMaterialTimecards from a dict
time_and_material_timecards_from_dict = TimeAndMaterialTimecards.from_dict(time_and_material_timecards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


