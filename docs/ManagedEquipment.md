# ManagedEquipment

Managed Equipment Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_project_id** | **int** | ID of the project the equipment is currently dispatched to | [optional] 
**name** | **str** | Name of the equipment | [optional] 
**serial_number** | **str** | Serial number of the equipment | [optional] 
**identification_number** | **str** | Identification number of the equipment | [optional] 
**description** | **str** | description of the equipment | [optional] 
**managed_equipment_make_id** | **int** | ID of the equipment make | [optional] 
**managed_equipment_model_id** | **int** | ID of the equipment model | [optional] 
**managed_equipment_type_id** | **int** | ID of the equipment type | [optional] 
**managed_equipment_category_id** | **int** | ID of the equipment category | [optional] 
**company_visible** | **bool** | Company visible | [optional] 
**year** | **int** | Year the equipment was manufactured in | [optional] 
**status** | **str** | Status | [optional] 
**ownership** | **str** | The type of ownership | [optional] 

## Example

```python
from procore_sdk.models.managed_equipment import ManagedEquipment

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipment from a JSON string
managed_equipment_instance = ManagedEquipment.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipment.to_json())

# convert the object into a dict
managed_equipment_dict = managed_equipment_instance.to_dict()
# create an instance of ManagedEquipment from a dict
managed_equipment_from_dict = ManagedEquipment.from_dict(managed_equipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


