# TimeAndMaterialEntryBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_entry** | [**TimeAndMaterialEntry1**](TimeAndMaterialEntry1.md) |  | 

## Example

```python
from procore_sdk.models.time_and_material_entry_body import TimeAndMaterialEntryBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEntryBody from a JSON string
time_and_material_entry_body_instance = TimeAndMaterialEntryBody.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEntryBody.to_json())

# convert the object into a dict
time_and_material_entry_body_dict = time_and_material_entry_body_instance.to_dict()
# create an instance of TimeAndMaterialEntryBody from a dict
time_and_material_entry_body_from_dict = TimeAndMaterialEntryBody.from_dict(time_and_material_entry_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


