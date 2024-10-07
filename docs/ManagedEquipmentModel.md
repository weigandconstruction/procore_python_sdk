# ManagedEquipmentModel

Equipment Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name of the equipment model | [optional] 
**managed_equipment_make_id** | **int** | Equipment make ID the model is associated to | [optional] 
**managed_equipment_type_id** | **int** | Equipment type ID the model is associated to | [optional] 
**company_id** | **int** | Company ID | [optional] 
**is_active** | **bool** | Is Active | [optional] 
**updated_at** | **datetime** | Date the equipment model was updated | [optional] 
**created_at** | **datetime** | Date the equipment model was created | [optional] 
**deleted_at** | **datetime** | Date the equipment model was deleted | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**managed_equipment_make** | [**ManagedEquipmentMake**](ManagedEquipmentMake.md) |  | [optional] 
**managed_equipment_type** | [**ManagedEquipmentType**](ManagedEquipmentType.md) |  | [optional] 

## Example

```python
from procore_sdk.models.managed_equipment_model import ManagedEquipmentModel

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentModel from a JSON string
managed_equipment_model_instance = ManagedEquipmentModel.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentModel.to_json())

# convert the object into a dict
managed_equipment_model_dict = managed_equipment_model_instance.to_dict()
# create an instance of ManagedEquipmentModel from a dict
managed_equipment_model_from_dict = ManagedEquipmentModel.from_dict(managed_equipment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


