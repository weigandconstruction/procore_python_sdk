# TimeAndMaterialEntryBulkUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_entry** | [**TimeAndMaterialEntry2**](TimeAndMaterialEntry2.md) |  | 

## Example

```python
from procore_sdk.models.time_and_material_entry_bulk_update_body import TimeAndMaterialEntryBulkUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEntryBulkUpdateBody from a JSON string
time_and_material_entry_bulk_update_body_instance = TimeAndMaterialEntryBulkUpdateBody.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEntryBulkUpdateBody.to_json())

# convert the object into a dict
time_and_material_entry_bulk_update_body_dict = time_and_material_entry_bulk_update_body_instance.to_dict()
# create an instance of TimeAndMaterialEntryBulkUpdateBody from a dict
time_and_material_entry_bulk_update_body_from_dict = TimeAndMaterialEntryBulkUpdateBody.from_dict(time_and_material_entry_bulk_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


