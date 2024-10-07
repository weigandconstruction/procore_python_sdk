# RestV10ProjectsProjectIdMaterialsGet200ResponseInner

Material

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name of the material | [optional] 
**description** | **str** | Description of the material | [optional] 
**uom** | **str** | Unit of measure | [optional] 
**quantity** | **float** | Quantity | [optional] 
**project_id** | **int** | ID of the project the material was logged for | [optional] 
**time_and_material_entry_id** | **int** | Time And Material Entry ID the material is associated with | [optional] 
**updated_at** | **datetime** | Date the Material was updated | [optional] 
**created_at** | **datetime** | Date the Material was created | [optional] 
**deleted_at** | **datetime** | Date the Material was deleted | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_materials_get200_response_inner import RestV10ProjectsProjectIdMaterialsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdMaterialsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_materials_get200_response_inner_instance = RestV10ProjectsProjectIdMaterialsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdMaterialsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_materials_get200_response_inner_dict = rest_v10_projects_project_id_materials_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdMaterialsGet200ResponseInner from a dict
rest_v10_projects_project_id_materials_get200_response_inner_from_dict = RestV10ProjectsProjectIdMaterialsGet200ResponseInner.from_dict(rest_v10_projects_project_id_materials_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


