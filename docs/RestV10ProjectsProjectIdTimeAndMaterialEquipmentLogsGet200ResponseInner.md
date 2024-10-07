# RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner

Time And Material Equipment Log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**description** | **str** | Discription of Time And Material Equipment Log | [optional] 
**uom** | **str** | Unit of measure for associate Time And Material Equipment Log | [optional] 
**quantity** | **int** | Number of Time And Material Equipment Log used | [optional] 
**project_id** | **int** | ID of the project the Time And Material Equipment Log was logged on | [optional] 
**time_and_material_entry_id** | **int** | Time And Material Entry ID the Time And Material Equipment Log is associated with | [optional] 
**updated_at** | **datetime** | Date the Time And Material Equipment Log was updated | [optional] 
**created_at** | **datetime** | Date the Time And Material Equipment Log was created | [optional] 
**deleted_at** | **datetime** | Date the Time And Material Equipment Log was deleted | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner_instance = RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner_dict = rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


