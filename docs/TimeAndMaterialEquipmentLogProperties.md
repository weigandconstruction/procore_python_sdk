# TimeAndMaterialEquipmentLogProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_and_material_entry_id** | **int** | Time &amp; Material Entry Id of Time And Material Equipment Log | [optional] 
**description** | **str** | Description of Time And Material Equipment Log | [optional] 
**uom** | **str** | Unit of measure for Time And Material Equipment Log | [optional] 
**quantity** | **int** | Quantity of Time And Material Equipment Log | [optional] 

## Example

```python
from procore_sdk.models.time_and_material_equipment_log_properties import TimeAndMaterialEquipmentLogProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndMaterialEquipmentLogProperties from a JSON string
time_and_material_equipment_log_properties_instance = TimeAndMaterialEquipmentLogProperties.from_json(json)
# print the JSON string representation of the object
print(TimeAndMaterialEquipmentLogProperties.to_json())

# convert the object into a dict
time_and_material_equipment_log_properties_dict = time_and_material_equipment_log_properties_instance.to_dict()
# create an instance of TimeAndMaterialEquipmentLogProperties from a dict
time_and_material_equipment_log_properties_from_dict = TimeAndMaterialEquipmentLogProperties.from_dict(time_and_material_equipment_log_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


