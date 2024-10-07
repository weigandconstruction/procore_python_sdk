# ManagedEquipmentType

Equipment Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name of the equipment Type | [optional] 
**managed_equipment_category_id** | **int** | Equipment category ID the type is associated with | [optional] 
**company_id** | **int** | Company ID | [optional] 
**is_active** | **bool** | Is Active | [optional] 
**updated_at** | **datetime** | Date the equipment type was updated | [optional] 
**created_at** | **datetime** | Date the equipment type was created | [optional] 
**deleted_at** | **datetime** | Date the equipment type was deleted | [optional] 
**managed_equipment_category** | [**ManagedEquipmentCategory**](ManagedEquipmentCategory.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.managed_equipment_type import ManagedEquipmentType

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentType from a JSON string
managed_equipment_type_instance = ManagedEquipmentType.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentType.to_json())

# convert the object into a dict
managed_equipment_type_dict = managed_equipment_type_instance.to_dict()
# create an instance of ManagedEquipmentType from a dict
managed_equipment_type_from_dict = ManagedEquipmentType.from_dict(managed_equipment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


