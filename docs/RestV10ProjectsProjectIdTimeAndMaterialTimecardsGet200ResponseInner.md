# RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner

Time And Material Timecard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**hours_worked** | **float** | Quantity | [optional] 
**company_id** | **int** | Company ID | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**time_and_material_entry_id** | **int** | Time And Material Entry ID the timecard is associated with | [optional] 
**timecard_time_type_id** | **int** | Type ID for the timecard | [optional] 
**work_classification_id** | **int** | Work classification id for the worker | [optional] 
**updated_at** | **datetime** | Date the Material was updated | [optional] 
**created_at** | **datetime** | Date the Material was created | [optional] 
**deleted_at** | **datetime** | Date the Material was deleted | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner_instance = RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner_dict = rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner from a dict
rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner_from_dict = RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.from_dict(rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


