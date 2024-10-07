# ManagedEquipmentSerialNumberUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_equipment** | [**ManagedEquipment1**](ManagedEquipment1.md) |  | 

## Example

```python
from procore_sdk.models.managed_equipment_serial_number_update_body import ManagedEquipmentSerialNumberUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentSerialNumberUpdateBody from a JSON string
managed_equipment_serial_number_update_body_instance = ManagedEquipmentSerialNumberUpdateBody.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentSerialNumberUpdateBody.to_json())

# convert the object into a dict
managed_equipment_serial_number_update_body_dict = managed_equipment_serial_number_update_body_instance.to_dict()
# create an instance of ManagedEquipmentSerialNumberUpdateBody from a dict
managed_equipment_serial_number_update_body_from_dict = ManagedEquipmentSerialNumberUpdateBody.from_dict(managed_equipment_serial_number_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


