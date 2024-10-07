# TimeAndMaterialEquipmentLogs

Equipment log Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_equipment_logs_ids** | **List[int]** | Array of time and material equipment log IDs specified for delete | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_equipment_logs import TimeAndMaterialEquipmentLogs

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEquipmentLogs from a JSON string
time_and_material_equipment_logs_instance = TimeAndMaterialEquipmentLogs.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEquipmentLogs.to_json())

# convert the object into a dict
time_and_material_equipment_logs_dict = time_and_material_equipment_logs_instance.to_dict()
# create an instance of TimeAndMaterialEquipmentLogs from a dict
time_and_material_equipment_logs_from_dict = TimeAndMaterialEquipmentLogs.from_dict(time_and_material_equipment_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


