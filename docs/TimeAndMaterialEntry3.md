# TimeAndMaterialEntry3

Time and Material Entry Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equipment_name** | **str** | Equipment Name | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_entry3 import TimeAndMaterialEntry3

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEntry3 from a JSON string
time_and_material_entry3_instance = TimeAndMaterialEntry3.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEntry3.to_json())

# convert the object into a dict
time_and_material_entry3_dict = time_and_material_entry3_instance.to_dict()
# create an instance of TimeAndMaterialEntry3 from a dict
time_and_material_entry3_from_dict = TimeAndMaterialEntry3.from_dict(time_and_material_entry3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


