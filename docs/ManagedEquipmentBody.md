# ManagedEquipmentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_equipment** | [**ManagedEquipment**](ManagedEquipment.md) |  | 

## Example

```python
from procore_sdk.models.managed_equipment_body import ManagedEquipmentBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentBody from a JSON string
managed_equipment_body_instance = ManagedEquipmentBody.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentBody.to_json())

# convert the object into a dict
managed_equipment_body_dict = managed_equipment_body_instance.to_dict()
# create an instance of ManagedEquipmentBody from a dict
managed_equipment_body_from_dict = ManagedEquipmentBody.from_dict(managed_equipment_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


