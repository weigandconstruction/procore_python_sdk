# TimeAndMaterialTimecardProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_entry_id** | **int** | Time &amp; Material Entry Id the timecard is associated with | [optional] 
**timecard_time_type_id** | **int** | Type id for the type of timecard being created | [optional] 
**login_information_id** | **int** | ID of the person the timecard is being created for | [optional] 
**work_classification_id** | **int** | ID of the worker&#39;s work classification | [optional] 
**hours_worked** | **float** | Total hours worked | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_timecard_properties import TimeAndMaterialTimecardProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialTimecardProperties from a JSON string
time_and_material_timecard_properties_instance = TimeAndMaterialTimecardProperties.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialTimecardProperties.to_json())

# convert the object into a dict
time_and_material_timecard_properties_dict = time_and_material_timecard_properties_instance.to_dict()
# create an instance of TimeAndMaterialTimecardProperties from a dict
time_and_material_timecard_properties_from_dict = TimeAndMaterialTimecardProperties.from_dict(time_and_material_timecard_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


