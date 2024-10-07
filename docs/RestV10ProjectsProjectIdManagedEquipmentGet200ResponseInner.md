# RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner

Managed Equipment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | The name of the install managed equipment | [optional] 
**company_id** | **int** | The Comapny ID the Managed Equipment was created with | [optional] 
**current_project_id** | **int** | Project ids the equipment is involved in | [optional] 
**company_visible** | **bool** | Is the equipment visible as a company equipment | [optional] 
**updated_at** | **datetime** | Date the managed equipment was updated | [optional] 
**created_at** | **datetime** | Date the managed equipment was created | [optional] 
**deleted_at** | **datetime** | Date the managed equipment was deleted | [optional] 
**serial_number** | **str** | Serial number of the equipment | [optional] 
**identification_number** | **str** | Identification number of the equipment | [optional] 
**description** | **str** | description of the equipment | [optional] 
**managed_equipment_make_id** | **int** | ID of the equipment make | [optional] 
**managed_equipment_model_id** | **int** | ID of the equipment model | [optional] 
**managed_equipment_type_id** | **int** | ID of the equipment type | [optional] 
**managed_equipment_category_id** | **int** | ID of the equipment category | [optional] 
**year** | **int** | Year the equipment was manufactured in | [optional] 
**status** | **str** | Status | [optional] 
**ownership** | **str** | The type of ownership | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**managed_equipment_make** | [**ManagedEquipmentMake**](ManagedEquipmentMake.md) |  | [optional] 
**managed_equipment_model** | [**ManagedEquipmentModel**](ManagedEquipmentModel.md) |  | [optional] 
**managed_equipment_category** | [**ManagedEquipmentCategory**](ManagedEquipmentCategory.md) |  | [optional] 
**managed_equipment_type** | [**ManagedEquipmentType**](ManagedEquipmentType.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_managed_equipment_get200_response_inner import RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner from a JSON string
rest_v10_projects_project_id_managed_equipment_get200_response_inner_instance = RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_managed_equipment_get200_response_inner_dict = rest_v10_projects_project_id_managed_equipment_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner from a dict
rest_v10_projects_project_id_managed_equipment_get200_response_inner_from_dict = RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.from_dict(rest_v10_projects_project_id_managed_equipment_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


