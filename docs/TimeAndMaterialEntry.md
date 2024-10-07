# TimeAndMaterialEntry

Timecard Time Type Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_rate** | **bool** | The pay_rate of the Timecard Time Type | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_entry import TimeAndMaterialEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEntry from a JSON string
time_and_material_entry_instance = TimeAndMaterialEntry.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEntry.to_json())

# convert the object into a dict
time_and_material_entry_dict = time_and_material_entry_instance.to_dict()
# create an instance of TimeAndMaterialEntry from a dict
time_and_material_entry_from_dict = TimeAndMaterialEntry.from_dict(time_and_material_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


