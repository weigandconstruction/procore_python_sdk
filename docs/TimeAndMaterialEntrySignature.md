# TimeAndMaterialEntrySignature

Time and Material Entry Signature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_signature_ids** | **List[int]** |  | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_entry_signature import TimeAndMaterialEntrySignature

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEntrySignature from a JSON string
time_and_material_entry_signature_instance = TimeAndMaterialEntrySignature.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEntrySignature.to_json())

# convert the object into a dict
time_and_material_entry_signature_dict = time_and_material_entry_signature_instance.to_dict()
# create an instance of TimeAndMaterialEntrySignature from a dict
time_and_material_entry_signature_from_dict = TimeAndMaterialEntrySignature.from_dict(time_and_material_entry_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


