# TimeAndMaterialSignatureBulkDestroy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_entry** | [**TimeAndMaterialEntrySignature**](TimeAndMaterialEntrySignature.md) |  | 

## Example

```python
from procore_sdk.models.time_and_material_signature_bulk_destroy import TimeAndMaterialSignatureBulkDestroy

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialSignatureBulkDestroy from a JSON string
time_and_material_signature_bulk_destroy_instance = TimeAndMaterialSignatureBulkDestroy.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialSignatureBulkDestroy.to_json())

# convert the object into a dict
time_and_material_signature_bulk_destroy_dict = time_and_material_signature_bulk_destroy_instance.to_dict()
# create an instance of TimeAndMaterialSignatureBulkDestroy from a dict
time_and_material_signature_bulk_destroy_from_dict = TimeAndMaterialSignatureBulkDestroy.from_dict(time_and_material_signature_bulk_destroy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


