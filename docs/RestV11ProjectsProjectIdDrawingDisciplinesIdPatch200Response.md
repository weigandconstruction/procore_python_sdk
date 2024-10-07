# RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response

Drawing Discipline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Discipline ID | [optional] 
**name** | **str** | Drawing Discipline name | [optional] 
**position** | **int** | Position of the discipline in the drawing log | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_drawing_disciplines_id_patch200_response import RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response from a JSON string
rest_v11_projects_project_id_drawing_disciplines_id_patch200_response_instance = RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_drawing_disciplines_id_patch200_response_dict = rest_v11_projects_project_id_drawing_disciplines_id_patch200_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response from a dict
rest_v11_projects_project_id_drawing_disciplines_id_patch200_response_from_dict = RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response.from_dict(rest_v11_projects_project_id_drawing_disciplines_id_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


