# ManagedEquipmentCategory

Equipment Category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name of the equipment category | [optional] 
**company_id** | **int** | Company ID | [optional] 
**is_active** | **bool** | If the category is currently active | [optional] 
**updated_at** | **datetime** | Date the equipment category was updated | [optional] 
**created_at** | **datetime** | Date the equipment category was created | [optional] 
**deleted_at** | **datetime** | Date the equipment category was deleted | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.managed_equipment_category import ManagedEquipmentCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentCategory from a JSON string
managed_equipment_category_instance = ManagedEquipmentCategory.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentCategory.to_json())

# convert the object into a dict
managed_equipment_category_dict = managed_equipment_category_instance.to_dict()
# create an instance of ManagedEquipmentCategory from a dict
managed_equipment_category_from_dict = ManagedEquipmentCategory.from_dict(managed_equipment_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


