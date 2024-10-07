# ManagedEquipmentMake

Equipment Make

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name of the equipment make | [optional] 
**company_id** | **int** | Company ID | [optional] 
**is_active** | **bool** | if the equipment make is currently active | [optional] 
**updated_at** | **datetime** | Date the equipment make was updated | [optional] 
**created_at** | **datetime** | Date the equipment make was created | [optional] 
**deleted_at** | **datetime** | Date the equipment make was deleted | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.managed_equipment_make import ManagedEquipmentMake

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentMake from a JSON string
managed_equipment_make_instance = ManagedEquipmentMake.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentMake.to_json())

# convert the object into a dict
managed_equipment_make_dict = managed_equipment_make_instance.to_dict()
# create an instance of ManagedEquipmentMake from a dict
managed_equipment_make_from_dict = ManagedEquipmentMake.from_dict(managed_equipment_make_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


