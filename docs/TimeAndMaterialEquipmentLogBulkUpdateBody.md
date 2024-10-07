# TimeAndMaterialEquipmentLogBulkUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_equipment_logs** | [**List[TimeAndMaterialEquipmentLogProperties]**](TimeAndMaterialEquipmentLogProperties.md) | Array of Time and material equipment log objects | 

## Example

```python
from procore_sdk.models.time_and_material_equipment_log_bulk_update_body import TimeAndMaterialEquipmentLogBulkUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEquipmentLogBulkUpdateBody from a JSON string
time_and_material_equipment_log_bulk_update_body_instance = TimeAndMaterialEquipmentLogBulkUpdateBody.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEquipmentLogBulkUpdateBody.to_json())

# convert the object into a dict
time_and_material_equipment_log_bulk_update_body_dict = time_and_material_equipment_log_bulk_update_body_instance.to_dict()
# create an instance of TimeAndMaterialEquipmentLogBulkUpdateBody from a dict
time_and_material_equipment_log_bulk_update_body_from_dict = TimeAndMaterialEquipmentLogBulkUpdateBody.from_dict(time_and_material_equipment_log_bulk_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


