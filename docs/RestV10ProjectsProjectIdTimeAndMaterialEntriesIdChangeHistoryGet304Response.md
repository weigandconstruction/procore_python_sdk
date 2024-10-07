# RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response

Change History

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**column** | **str** | Name of the column changed | [optional] 
**readable_column** | **str** | Localized readable name of the column changed | [optional] 
**formatted_column** | **str** | Human readable name of the column changed | [optional] 
**old_value** | **str** | Value of the column before change | [optional] 
**new_value** | **str** | Value of the column after change | [optional] 
**created_by** | [**RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304ResponseCreatedBy**](RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304ResponseCreatedBy.md) |  | [optional] 
**created_at** | **datetime** | Created date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_id_change_history_get304_response import RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response from a JSON string
rest_v10_projects_project_id_time_and_material_entries_id_change_history_get304_response_instance = RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_time_and_material_entries_id_change_history_get304_response_dict = rest_v10_projects_project_id_time_and_material_entries_id_change_history_get304_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response from a dict
rest_v10_projects_project_id_time_and_material_entries_id_change_history_get304_response_from_dict = RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response.from_dict(rest_v10_projects_project_id_time_and_material_entries_id_change_history_get304_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


